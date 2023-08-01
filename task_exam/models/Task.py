from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
from datetime import datetime

class Task(models.Model):
    _name='task'
    _description = 'Task'

    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")
    assigned_to=fields.Many2one('res.partner',string='Assigned To' )
    deadline=fields.Datetime(string='deadline')
    categories=fields.Many2many('task.category',string='Categories')

    #  check if the task deadline is in the past, it should raise an error.
    @api.constrains('deadline')
    def _check_deadline(self):
        now = datetime.now()
        for task in self:
            if task.deadline and task.deadline < now:
                raise ValidationError("Task deadline cannot be in the past.")
