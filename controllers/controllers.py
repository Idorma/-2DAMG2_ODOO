# -*- coding: utf-8 -*-
from odoo import http

# class Lauserri(http.Controller):
#     @http.route('/lauserri/lauserri/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/lauserri/lauserri/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('lauserri.listing', {
#             'root': '/lauserri/lauserri',
#             'objects': http.request.env['lauserri.lauserri'].search([]),
#         })

#     @http.route('/lauserri/lauserri/objects/<model("lauserri.lauserri"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('lauserri.object', {
#             'object': obj
#         })