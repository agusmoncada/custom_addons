{
    'name': 'Color Change',
    'version': '1.0',
    'category': 'Customization',
    'summary': 'Change the color of the main top nav bar',
    'description': 'This module allows you to change the color of the main top nav bar in Odoo.',
    'author': 'Your Name',
    'depends': ['web'],
    'data': [
        'views/assets.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'color_change/static/src/css/custom_style.css',
        ],
    },
    'installable': True,
    'application': False,
}
