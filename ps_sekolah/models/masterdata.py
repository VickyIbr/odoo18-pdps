from odoo import models, fields

class MasterDataSiswa(models.Model):
    _name = "masterdata.siswa"
    _description = "Siswa"

    id = fields.One2many('konfigurasi.pembayaran.diskonkhusus','komponen',string='ID')
    name = fields.Char(string='Name')
    age = fields.Integer(string='Street')
    gender = fields.Char(string='Gender')
    classname = fields.Char(string='Class Name')
    address = fields.Char(string='Address')

