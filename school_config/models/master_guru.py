# -*- coding: utf-8 -*-

from odoo import models, fields, api

class MasterGuru(models.Model):
    _name = 'school_config.master.guru'
    _description = 'Master Data Guru'

    name = fields.Char(string="Nama Guru", required=True)

    _rec_name = 'name'  # optional if your field is already 'name'
