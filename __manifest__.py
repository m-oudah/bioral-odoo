# -*- coding: utf-8 -*-
{
    'name': "Bioral",

    'summary': """
       This module is for Bioral Company updates
       
       """,

    'description': """
        Long description of module's purpose
    """,

    'author': "Brandon IT Department - Mohammed Oudah",
    'website': "http://www.brandon-group.net",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale','base','product'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        # 'views/saleOrderReport.xml',
        'views/bioral_layout.xml',
        'views/reaya_layout.xml',
        'views/bioral_report_saleorder_document.xml',
        # 'views/saleUpdate.xml',
        # 'views/ProductUpdate.xml',
        # 'views/OrderLineUpdate.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
