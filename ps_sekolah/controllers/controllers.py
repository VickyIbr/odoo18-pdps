# -*- coding: utf-8 -*-
# from odoo import http


# class PsSekolah(http.Controller):
#     @http.route('/ps_sekolah/ps_sekolah', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ps_sekolah/ps_sekolah/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ps_sekolah.listing', {
#             'root': '/ps_sekolah/ps_sekolah',
#             'objects': http.request.env['ps_sekolah.ps_sekolah'].search([]),
#         })

#     @http.route('/ps_sekolah/ps_sekolah/objects/<model("ps_sekolah.ps_sekolah"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ps_sekolah.object', {
#             'object': obj
#         })

