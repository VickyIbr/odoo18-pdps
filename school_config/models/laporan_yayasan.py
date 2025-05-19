# -*- coding: utf-8 -*-

from odoo import models, fields, api

class LaporanYayasan(models.Model):
    _name = 'school_config.laporan.yayasan'
    _description = 'Laporan Ke Yayasan'
    _order = 'id asc'

    name = fields.Many2one(
        comodel_name='school_config.master.siswa',
        string='Nama Siswa',
        required=False,
    )
    nama_halaqah = fields.Char(string='Nama Halaqah')
    jumlah_santri = fields.Char(string='Jumlah Santri')
    total = fields.Char(string='Total')
    jenjang = fields.Char(string='Jenjang')
    jumlah = fields.Char(string='Jumlah')