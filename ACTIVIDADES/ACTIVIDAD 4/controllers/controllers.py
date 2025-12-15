# -*- coding: utf-8 -*-
# from odoo import http


# class Actividad4Ciclosformativos(http.Controller):
#     @http.route('/actividad4_ciclosformativos/actividad4_ciclosformativos', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/actividad4_ciclosformativos/actividad4_ciclosformativos/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('actividad4_ciclosformativos.listing', {
#             'root': '/actividad4_ciclosformativos/actividad4_ciclosformativos',
#             'objects': http.request.env['actividad4_ciclosformativos.actividad4_ciclosformativos'].search([]),
#         })

#     @http.route('/actividad4_ciclosformativos/actividad4_ciclosformativos/objects/<model("actividad4_ciclosformativos.actividad4_ciclosformativos"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('actividad4_ciclosformativos.object', {
#             'object': obj
#         })

