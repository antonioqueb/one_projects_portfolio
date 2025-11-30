from odoo import models, fields, api

class OneProject(models.Model):
    _name = 'one.project'
    _description = 'Portfolio Project'
    _order = 'id desc'

    name = fields.Char(string='Title', required=True, help="Mapped to JSON 'title'")
    slug = fields.Char(string='Slug (URL)', required=True, copy=False)
    
    # Campos específicos del Proyecto
    location = fields.Char(string='Location')
    category = fields.Char(string='Category', help="Ej: Residential, Hospitality")
    year = fields.Char(string='Year', help="Ej: 2024")
    
    # Campos opcionales para el detalle
    architect = fields.Char(string='Architect')
    client_name = fields.Char(string='Client') # 'client' es palabra reservada en algunos contextos, usamos client_name

    # Descripciones
    description_short = fields.Text(string='Short Description', help="Intro text (line-clamp-2)")
    description_long = fields.Html(string='Long Description (HTML)', sanitize=False)

    # --- IMAGEN PRINCIPAL ---
    image_file = fields.Image(string="Main Image Upload", max_width=1920, max_height=1920)
    image_external_url = fields.Char(string="External Image URL", help="Fallback if no file uploaded")

    # Galería
    gallery_ids = fields.One2many('one.project.gallery', 'project_id', string='Gallery Images')

    _sql_constraints = [
        ('slug_unique', 'unique(slug)', 'The slug must be unique!')
    ]

    def get_image_url(self):
        """ Retorna URL local o externa """
        self.ensure_one()
        base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        if self.image_file:
            return f"{base_url}/web/image/one.project/{self.id}/image_file"
        return self.image_external_url or ""

class OneProjectGallery(models.Model):
    _name = 'one.project.gallery'
    _description = 'Project Gallery Image'
    _order = 'id'

    project_id = fields.Many2one('one.project', string='Project', ondelete='cascade')
    
    image_file = fields.Image(string="Gallery Image Upload", max_width=1920, max_height=1920)
    image_external_url = fields.Char(string="External URL")

    def get_gallery_url(self):
        self.ensure_one()
        base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        if self.image_file:
            return f"{base_url}/web/image/one.project.gallery/{self.id}/image_file"
        return self.image_external_url or ""
