# -*- coding: utf-8 -*-

from odoo import models, fields, api

class LaporanBulanan(models.Model):
    _name = 'school_config.laporan.bulanan'
    _description = 'Laporan Bulanan'

    nomor = fields.Char(string='Nomor')
    wali_kelas = fields.Char(string='Wali Kelas')
    group_by = fields.Char(string='Group By')
    operator = fields.Char(string='Operator')
    komponen = fields.Char(string='Komponen')