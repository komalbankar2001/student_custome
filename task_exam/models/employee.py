from odoo import api, fields, models, _

class EmployeeTask(models.Model):
    _name = "employee.task"
    _description = "Employee Task"

    name = fields.Char(string="Name", required=True)
    department = fields.Char(string="Department")
    email=fields.Char(string="Email")
    admission_count=fields.Integer(string='Admission_count',tracking=True,compute='_compute_admission_count')
    tasks=fields.One2many('employee.task','name' ,string='tasks')

    # calculate the total number of tasks assigned to the employee.
    def _compute_admission_count(self):
        for rec in self:
            admission_count = self.env['employee.task'].search_count([('admission_count', '=', rec.id)])
            print('count=================>>>>>>>>>>>>>>>>', admission_count)
            rec.admission_count = admission_count

