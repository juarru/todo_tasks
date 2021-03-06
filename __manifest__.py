# -*- coding: utf-8 -*-

{
    'name': 'To-Do tasks',
    'decription': 'Aplicación de listas To-Do',
    'summary': 'To_Do tasks',
    'version': '1.0',
    'license': 'LGPL-3',
    'author': 'Juan Arillo',
    'website': 'https://github.com/juarru/todo_tasks',
    'category': 'Uncategorized',
    'depends': ['base'],
    'application': True,
    'installable': True,
    'auto_install': False,
    'data': ['security/ir.model.access.csv',
             'security/todo_access_rules.xml',
             'views/todo_menu.xml',
             'views/todo_view.xml', ],
}
