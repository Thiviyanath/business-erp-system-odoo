{
    'name': 'Business ERP System',
    'version': '1.0',
    'summary': 'Custom ERP System',
    'description': 'ERP system for inventory and sales management',
    'author': 'Thiviyanath',
    'category': 'Business',
    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
        'views/product_views.xml',
        'views/customer_views.xml',
        'views/sales_views.xml',
        'views/dashboard_views.xml',
        'views/invoice_views.xml',
    ],

    'demo': [
        'demo/demo_data.xml',
    ],

    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}