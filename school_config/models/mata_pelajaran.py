# -*- coding: utf-8 -*-

from odoo import models, fields, api

class MataPelajaran(models.Model):
    _name = 'school_config.mata.pelajaran'
    _description = 'Mata Pelajaran'

    no_urut = fields.Char(string='No. Urut')
    name = fields.Char(string='Nama')
    lembaga = fields.Char(string='Lembaga')