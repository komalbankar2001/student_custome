from odoo import api, fields, models, _

class TaskComment(models.Model):
    _name = "task.comment"
    _description = "Task Comment"

    task = fields.Many2one('task',string="task")
    employee = fields.Many2one('employee.task', string="Employee")
    comment=fields.Text(string='comment')
    comment_date=fields.Datetime(string='Comment_Date')
