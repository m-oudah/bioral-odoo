# -*- coding: utf-8 -*-
# from odoo import http


# class Brandon(http.Controller):
#     @http.route('/brandon/brandon/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/brandon/brandon/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('brandon.listing', {
#             'root': '/brandon/brandon',
#             'objects': http.request.env['brandon.brandon'].search([]),
#         })

#     @http.route('/brandon/brandon/objects/<model("brandon.brandon"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('brandon.object', {
#             'object': obj
#         })
