# -*- coding: utf-8 -*-
# from odoo import http


# class Sumacarcer(http.Controller):
#     @http.route('/sumacarcer/sumacarcer/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sumacarcer/sumacarcer/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sumacarcer.listing', {
#             'root': '/sumacarcer/sumacarcer',
#             'objects': http.request.env['sumacarcer.sumacarcer'].search([]),
#         })

#     @http.route('/sumacarcer/sumacarcer/objects/<model("sumacarcer.sumacarcer"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sumacarcer.object', {
#             'object': obj
#         })
