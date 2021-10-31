# -*- coding: utf-8 -*-
# from odoo import http


# class SpaceshipsInvaders(http.Controller):
#     @http.route('/spaceships_invaders/spaceships_invaders/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/spaceships_invaders/spaceships_invaders/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('spaceships_invaders.listing', {
#             'root': '/spaceships_invaders/spaceships_invaders',
#             'objects': http.request.env['spaceships_invaders.spaceships_invaders'].search([]),
#         })

#     @http.route('/spaceships_invaders/spaceships_invaders/objects/<model("spaceships_invaders.spaceships_invaders"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('spaceships_invaders.object', {
#             'object': obj
#         })
