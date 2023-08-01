from odoo import api, fields, models, _

class TaskCategory(models.Model):
    _name = "task.category"
    _description = "Task Category"

    name = fields.Char(string="Name", required=True)
    projects = fields.Many2one('project', string="Description")
