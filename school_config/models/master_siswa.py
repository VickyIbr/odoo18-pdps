# -*- coding: utf-8 -*-

from odoo import models, fields, api

class MasterSiswa(models.Model):
    _name = 'school_config.master.siswa'
    _description = 'Master Data Siswa'

    name = fields.Char(string="Nama Siswa", required=True)

    _rec_name = 'name'  # optional if your field is already 'name'
