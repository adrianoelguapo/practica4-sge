# -*- coding: utf-8 -*-
# from odoo import http


# class Actividad3Hospital(http.Controller):
#     @http.route('/actividad3_hospital/actividad3_hospital', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/actividad3_hospital/actividad3_hospital/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('actividad3_hospital.listing', {
#             'root': '/actividad3_hospital/actividad3_hospital',
#             'objects': http.request.env['actividad3_hospital.actividad3_hospital'].search([]),
#         })

#     @http.route('/actividad3_hospital/actividad3_hospital/objects/<model("actividad3_hospital.actividad3_hospital"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('actividad3_hospital.object', {
#             'object': obj
#         })

