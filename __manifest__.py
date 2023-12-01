{
    'name': 'Odoo Custom Module',
    'version': '1.0',
    'category': 'Custom',
    'author': 'nando',
    'summary': 'Custom module',
    'description': "This is custom module",
    'depends': [],
    'data': [
        'views/menu.xml',
        'views/patient_view.xml',
        'views/room_view.xml',
        'security/ir.model.access.csv'
    ],
    'installable': True,

}