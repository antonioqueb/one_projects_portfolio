{
    'name': 'One Projects Portfolio API',
    'version': '1.0',
    'summary': 'Backend API for Projects/Portfolio (Next.js compatible)',
    'description': """
        Manage architectural/design projects.
        Exposes endpoints:
        - /api/projects
        - /api/projects/<slug>
    """,
    'category': 'Backend',
    'author': 'Tu Nombre',
    'depends': ['base', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'views/project_views.xml',
        'data/demo_data.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
    'icon': '/base/static/description/icon.png',
}
