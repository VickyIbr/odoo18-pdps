from odoo import models, fields

class MasterDataSiswa(models.Model):
    _name = "masterdata.siswa"
    _description = "Siswa"

    id = fields.One2many('konfigurasi.pembayaran.diskonkhusus','komponen',string='ID')
    name = fields.Char(string='Name', required=True)
    street = fields.Char(string='Street')
    street2 = fields.Char(string='Street 2')
    city = fields.Char(string='City')
    state_id = fields.Char(string='State ID')
    zip = fields.Char(string='ZIP')
    country_id = fields.Char(string='Country ID')
    vat = fields.Char(string='VAT')
    phone = fields.Char(string='Phone')
    mobile = fields.Char(string='Mobile')
    email = fields.Char(string='Email')
    website = fields.Char(string='Website')
    lang = fields.Char(string='Languange')

    # Field siswa

    # Informasi
    pendaftaran = fields.Char(string="Pendaftaran")
    jenjang = fields.Char(string="Jenjang")
    tahun_ajaran = fields.Char(string="Tahun Ajaran")
    nisq = fields.Char(string="NISQ")
    orang_tua = fields.Char(string="Orang Tua")
    virtual_account = fields.Char(string="Virtual Account")
    lembaga = fields.Char(string="Lembaga")
    ruang_kelas = fields.Char(string="Ruang Kelas")
    nisn = fields.Char(string="NISN")
    user_login = fields.Char(string="User Login")
    siswa = fields.Boolean(string="Siswa")

    # Kelahiran
    tanggal_lahir = fields.Date(string="Tanggal Lahir")
    tempat_lahir = fields.Char(string="Tempat")
    agama = fields.Selection([
        ('islam', 'Islam'),
        ('katolik', 'Katolik'),
        ('protestan', 'Protestan'),
        ('hindu', 'Hindu'),
        ('budha', 'Budha'),
    ], string="Agama", default='islam')
    kebangsaan = fields.Selection([
        ('wni', 'WNI'),
        ('wna', 'WNA'),
        ('wni_keturunan', 'WNI Keturunan'),
    ], string="Kebangsaan", default='wni')

    # Saudara
    anak_ke = fields.Integer(string="Anak Ke")
    tiri = fields.Integer(string="Tiri")
    kandung = fields.Integer(string="Kandung")
    angkat = fields.Integer(string="Angkat")

    # Lainnya
    nama_panggilan = fields.Char(string="Nama Panggilan", placeholder='Nama Panggilan...')
    bahasa_di_rumah = fields.Char(string="Bahasa di Rumah", default='Indonesia')
    transportasi = fields.Char(string="Mode Transportasi")
    jarak_sekolah = fields.Float(string="Jarak Sekolah (km)")
    bertempat_tinggal_pada = fields.Text(string="Bertempat Tinggal Pada", default='Orang Tua')
    jenis_kelamin = fields.Selection([
        ('laki', 'Laki-Laki'),
        ('perempuan', 'Perempuan')
    ], string="Jenis Kelamin")
    gol_darah = fields.Selection([
        ('a', 'A'),
        ('b', 'B'),
        ('ab', 'AB'),
        ('o', 'O'),
        ('-', '-')
    ], string="Gol Darah" ,default='a')
    berat_badan = fields.Float(string="Berat Badan (kg)")
    tinggi_badan = fields.Float(string="Tinggi Badan (cm)")

    # Field Orang Tua
    father_name = fields.Char(string="Nama Ayah")
    father_phone = fields.Char(string="No. HP")
    father_religion = fields.Selection([
        ('islam', 'Islam'),
        ('katolik', 'Katolik'),
        ('protestan', 'Protestan'),
        ('hindu', 'Hindu'),
        ('budha', 'Budha'),
    ], string="Agama", default='islam')
    father_income = fields.Char(string="Penghasilan")
    father_education = fields.Char(string="Pendidikan")
    father_work = fields.Char(string="Pekerjaan")
    father_nationality = fields.Selection([
        ('wni', 'WNI'),
        ('wna', 'WNA'),
        ('wni_keturunan', 'WNI Keturunan'),
    ], string="Kebangsaan", default='wni')

    mother_name = fields.Char(string="Nama Ibu")
    mother_phone = fields.Char(string="No. HP")
    mother_religion = fields.Selection([
        ('islam', 'Islam'),
        ('katolik', 'Katolik'),
        ('protestan', 'Protestan'),
        ('hindu', 'Hindu'),
        ('budha', 'Budha'),
    ], string="Agama", default='islam')
    mother_income = fields.Char(string="Penghasilan")
    mother_education = fields.Char(string="Pendidikan")
    mother_work = fields.Char(string="Pekerjaan")
    mother_nationality = fields.Selection([
        ('wni', 'WNI'),
        ('wna', 'WNA'),
        ('wni_keturunan', 'WNI Keturunan'),
    ], string="Kebangsaan", default='wni')

    wali_name = fields.Char(string="Nama Wali")
    wali_phone = fields.Char(string="No. HP")
    wali_religion = fields.Selection([
        ('islam', 'Islam'),
        ('katolik', 'Katolik'),
        ('protestan', 'Protestan'),
        ('hindu', 'Hindu'),
        ('budha', 'Budha'),
    ], string="Agama", default='islam')
    wali_income = fields.Char(string="Penghasilan")
    wali_education = fields.Char(string="Pendidikan")
    wali_work = fields.Char(string="Pekerjaan")
    wali_nationality = fields.Selection([
        ('wni', 'WNI'),
        ('wna', 'WNA'),
        ('wni_keturunan', 'WNI Keturunan'),
    ], string="Kebangsaan", default='wni')

    # Tab Harga Khusus

    bebas_biaya = fields.Boolean(string="Bebas Biaya")
    komponen_ids = fields.Many2many(
        'konfigurasi.pembayaran.komponenusaha',
        'siswa_komponen_rel',
        'siswa_id',
        'komponen_id',
        String="Komponen"

    )
    

