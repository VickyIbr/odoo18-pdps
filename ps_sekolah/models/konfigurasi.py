from odoo import models, fields

class KonfigurasiSekolahLaporanBulanan(models.Model):
    _name = "konfigurasi.sekolah.laporanbulanan"
    _description = "Laporan Bulanan"

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


class KonfigurasiPembayaranPeriods(models.Model):
    _name = "konfigurasi.pembayaran.periods"
    _description = "Periods"

    name = fields.Char(string='Period Name')
    code = fields.Char(string='Code')
    fiscal_year_id = fields.Many2one('konfigurasi.pembayaran.tahunajaran', string='Fiscal Year')
    openingclosingperiod = fields.Boolean(string='Opening/Closing Period', default=False)
    startdate = fields.Date(string='Start Date')
    enddate = fields.Date(string='End Date')

class KonfigurasiPembayaranKomponenUsaha(models.Model):
    _name = "konfigurasi.pembayaran.komponenusaha"
    _description = "Komponen Usaha"

    name = fields.Char(string='Nama')
    payment = fields.Selection([
        ('credit', 'Credit'),
        ('cash', 'Cash'),
    ], string='Payment', default='cash')
    jemputan = fields.Boolean(string='Jemputan')
    tujuan = fields.Selection([
        ('yayasan', 'Yayasan'),
        ('sekolah', 'Sekolah'),
    ], string='Tujuan')
    catering = fields.Boolean(string='Catering')
    active = fields.Boolean(string='Active', default='true')

class KonfigurasiPembayaranDiskonKhusus(models.Model):
    _name = "konfigurasi.pembayaran.diskonkhusus"
    _description = "Diskon Khusus"

    siswa_id = fields.Many2one('masterdata.siswa', string='Siswa')
    komponen_id = fields.Many2one('konfigurasi.pembayaran.komponenusaha', string='Komponen')
    keterangan = fields.Text(string='Keterangan')
    diskon_amount = fields.Integer(string='Disc Amount')
    diskon_percent = fields.Integer(string='Disc Percent')
