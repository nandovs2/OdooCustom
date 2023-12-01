from odoo import fields, models, api


class HospitalRoom(models.Model):
    _name = 'hospital.room'
    _description = 'Hospital Room'

    name = fields.Char(string='Name')
    no = fields.Integer(string='Number')
