from odoo import fields, models, api


class HospitalPatient(models.Model):
    _name = 'hospital.patient' #nama dari model/tabel
    _description = 'Hospital Patient' #deskripsi model/tabel

    #field dari model/tabel (column)
    name = fields.Char(string='Name')
    age = fields.Integer(string='Age')
    gender = fields.Selection([('male','Male'),('female','Female')],string='Gender')
