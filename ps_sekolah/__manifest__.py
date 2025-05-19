# -*- coding: utf-8 -*-
{
    'name': "Sekolah",

    'summary': "Modul Sekolah",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Education',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],
    'license': 'LGPL-3',

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        # 'views/konfigurasi/sekolah/laporanbulanan_views.xml',
        # 'views/konfigurasi/sekolah/laporankeyayasan_views.xml',
        # 'views/konfigurasi/sekolah/matapelajaran_views.xml',
        # 'views/konfigurasi/sekolah/rombel_views.xml',
        'views/konfigurasi/pembayaran/periods_views.xml',
        'views/konfigurasi/pembayaran/tahunajaran_views.xml',
        'views/konfigurasi/pembayaran/komponenusaha_views.xml',
        'views/konfigurasi/pembayaran/diskonkhusus_views.xml',
        'views/masterdata/siswa_views.xml',
        'views/menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'installable': True,
}

