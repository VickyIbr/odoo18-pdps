from odoo import models, fields, api

class DaftarSurat(models.Model):
    _name = 'school_config.daftar.surat'
    _description = 'Daftar Surat'

    nomor = fields.Char(string='No')
    nama = fields.Char(string='Nama')
    terjemah = fields.Char(string='Terjemah')
    jumlah_ayat = fields.Char(string='Jumlah Ayat')
    tempat = fields.Char(string='Tempat')
    juz = fields.Char(string='Juz')
    materi_kuadran_SD = fields.Char(string='Materi Kuadran SD')
    materi_kuadran_TK = fields.Char(string='Materi Kuadran TK')