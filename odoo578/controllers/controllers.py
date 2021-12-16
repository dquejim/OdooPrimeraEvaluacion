# -*- coding: utf-8 -*-
# from odoo import http


# class Odoo578(http.Controller):
#     @http.route('/odoo578/odoo578/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo578/odoo578/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo578.listing', {
#             'root': '/odoo578/odoo578',
#             'objects': http.request.env['odoo578.odoo578'].search([]),
#         })

#     @http.route('/odoo578/odoo578/objects/<model("odoo578.odoo578"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo578.object', {
#             'object': obj
#         })
