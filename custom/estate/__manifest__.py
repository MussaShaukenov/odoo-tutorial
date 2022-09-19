{
    'name': 'Real Estate',
    'version': '1.0',
    'description': "Real Estate app",
    'category': 'Custom',
    'website': 'https://www.youtube.com/?themeRefresh=1',
    'depends': [
        'base'
    ],
    'data': [
        'security/ir.model.access.csv',

        'views/estate_property_views.xml',
        'views/estate_menus.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3'
}