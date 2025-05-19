# -*- coding: utf-8 -*-

from odoo import models, fields, api

class KonfigurasiPembayaranTahunAjaran(models.Model):
    _name = "konfigurasi.pembayaran.tahunajaran"
    _description = "Tahun Ajaran"
    _rec_name = 'fiscal_year'

    fiscal_year = fields.Char(string='Fiscal Year')
    code = fields.Char(string='Code')
    startdate = fields.Date(string='Start Date')
    enddate = fields.Date(string='End Date')
    status = fields.Selection([('open', 'Open'),], string='Status', default='open')

    def name_get(self):
        result = []
        for record in self:
            label = record.fiscal_year or 'No Fiscal Year'
            result.append((record.id, label))
        return result