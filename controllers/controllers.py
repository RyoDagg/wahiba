# -*- coding: utf-8 -*-
# from odoo import http


# class Wahiba(http.Controller):
#     @http.route('/wahiba/wahiba/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/wahiba/wahiba/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('wahiba.listing', {
#             'root': '/wahiba/wahiba',
#             'objects': http.request.env['wahiba.wahiba'].search([]),
#         })

#     @http.route('/wahiba/wahiba/objects/<model("wahiba.wahiba"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('wahiba.object', {
#             'object': obj
#         })
