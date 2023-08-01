from odoo import api, fields, models, _

class Project(models.Model):
    _name = "project"
    _description = "Project"

    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")
    employeess=fields.Many2many('employee.task',string='employeess')


