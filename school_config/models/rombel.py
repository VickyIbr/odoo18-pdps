# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Rombel(models.Model):
    _name = 'school_config.rombel'
    _description = 'Rombel'

    name = fields.Char(string='Nama')
    lembaga_id = fields.Selection([
        ('smp', 'SMP'),
        ('sma', 'SMA')
    ] , string='Lembaga')
    grade = fields.Selection([
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12')
    ] , string='Grade')
    jenis = fields.Selection([
        ('banin', 'Banin'),
        ('banat', 'Banat'),
    ] , string='Jenis')
    walas_id = fields.Many2one(
        comodel_name='school_config.master.guru',
        string='Wali Kelas',
        required=False,
    )
    fiscal_year_id = fields.Many2one('konfigurasi.pembayaran.tahunajaran', string='Fiscal Year')