from odoo import models, fields, api

class PenugasanGuru(models.Model):
    _name = 'school_config.penugasan.guru'
    _description = 'Penugasan Guru'

    nomor_dokumen = fields.Char(string='No. Dokumen')
    lembaga = fields.Char(string='Lembaga')
    tahun_ajaran = fields.Char(string='Tahun Ajaran')
    rombel = fields.Char(string='Rombel')
    grade = fields.Char(string='Grade')
    guru = fields.Char(string='Guru')
    bidang_guru = fields.Char(string='Bidang Guru')
    wali_kelas_validator = fields.Char(string='Wali Kelas?')
    penguji_validator = fields.Char(string='Penguji?')
    halaqah_qount = fields.Char(string='Halaqah Qount')
    status = fields.Char(string='Status') 