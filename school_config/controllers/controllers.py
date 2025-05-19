# -*- coding: utf-8 -*-
# from odoo import http


# class ModulBaru(http.Controller):
#     @http.route('/modul_baru/modul_baru', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modul_baru/modul_baru/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('modul_baru.listing', {
#             'root': '/modul_baru/modul_baru',
#             'objects': http.request.env['modul_baru.modul_baru'].search([]),
#         })

#     @http.route('/modul_baru/modul_baru/objects/<model("modul_baru.modul_baru"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modul_baru.object', {
#             'object': obj
#         })

