# -*- coding: utf-8 -*-
{
    'name': "fix bill qty odoo 13",
    'version': '.0.1',
    'category': 'Purchase',
        "author": 'Zero Systems',
        "company": 'Zero for Information Systems',
         "website": "https://www.erpzero.com",
        "email": "sales@erpzero.com",
	"sequence": 0,

    'summary': """fix bug in Quantity field on Bill """,

    'description': """
        when create Bill from purshase order odoo13 couldn't record orderd QTY or Done QTY to Bill Quantity field 
        so this addon to fix this Bug.
    """,
    'depends': ['base','account', 'purchase'],
    'data': [
        'views/views.xml',
        'views/templates.xml',
    ],
	"auto_install": False,
	"installable": True,
	"application": False,
    'images': ['static/description/logo.PNG'],
	'license': 'LGPL-3',
}
