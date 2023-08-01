# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Task Exam',
    'version': '1.1',
    'summary': 'Task Exam System',
    'sequence': 10,
    'description': """ Task Exam System""",
    'category': 'Productivity',
    'website': 'https://www.odoomates.tech',
    'depends': [],
    'data': ['security/ir.model.access.csv','views/employee.xml','views/Task.xml','views/project.xml','views/TaskCategory.xml','views/TaskComment.xml'],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
