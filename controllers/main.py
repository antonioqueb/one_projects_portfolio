from odoo import http
from odoo.http import request, Response
import json

class OneProjectsController(http.Controller):

    @http.route(['/api/projects', '/api/projects/list'], type='http', auth='public', methods=['GET'], cors='*')
    def get_projects_list(self, **kwargs):
        projects = request.env['one.project'].sudo().search([])
        
        data_list = []
        for p in projects:
            data_list.append({
                "id": p.id,
                "slug": p.slug,
                "title": p.name,
                "location": p.location or "",
                "category": p.category or "",
                "year": p.year or "",
                "description": p.description_short or "",
                "image": p.get_image_url()
            })

        response = {"data": data_list}
        return Response(json.dumps(response), headers={'Content-Type': 'application/json'})

    @http.route('/api/projects/<string:slug>', type='http', auth='public', methods=['GET'], cors='*')
    def get_project_detail(self, slug, **kwargs):
        project = request.env['one.project'].sudo().search([('slug', '=', slug)], limit=1)

        if not project:
            return Response(json.dumps({"error": "Project not found"}), status=404, headers={'Content-Type': 'application/json'})

        # Array simple de strings para la galería
        gallery_urls = [g.get_gallery_url() for g in project.gallery_ids]

        project_data = {
            "id": project.id,
            "slug": project.slug,
            "title": project.name,
            "location": project.location or "",
            "category": project.category or "",
            "year": project.year or "",
            "image": project.get_image_url(),
            # Campos opcionales del detalle
            "architect": project.architect or "",
            "client": project.client_name or "",
            # Descripciones
            "description": project.description_short or "", # Subtítulo grande en el detalle
            "long_description": project.description_long or "", # HTML content
            "gallery": gallery_urls
        }

        response = {"data": project_data}
        return Response(json.dumps(response), headers={'Content-Type': 'application/json'})
