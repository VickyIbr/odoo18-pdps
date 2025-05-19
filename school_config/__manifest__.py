# -*- coding: utf-8 -*-
{
    'name': "School Configuration",
    'summary': "manage school configuration",
    'description': """
Long description of module's purpose
    """,
    'author': "My Company",
    'website': "https://www.yourcompany.com",
    'category': 'Education',  # Update category for better organization
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/Konfigurasi/Sekolah/laporan_yayasan_views.xml',
        'views/Konfigurasi/Sekolah/laporan_bulanan_views.xml',
        'views/Konfigurasi/Sekolah/rombel_views.xml',
        'views/Konfigurasi/Sekolah/mata_pelajaran_views.xml',
        'views/Konfigurasi/Pembayaran/tahun_ajaran_views.xml',
        'views/Konfigurasi/Tahfidz/penugasan_guru_views.xml',
        'views/Konfigurasi/Tahfidz/daftar_surat_views.xml',
        'views/Master_Data/siswa_views.xml',
        'views/Master_Data/guru_views.xml',
        'views/menu_views.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,  # This ensures the module appears in the Apps list
    'application': True,  # If it's a full-fledged application
    'auto_install': False,
}
