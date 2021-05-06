# -*- coding: utf-8 -*-
from odoo import http
import json


class DesignSpirit(http.Controller):
    @http.route('/contact_design_agent', methods=['POST'], auth="public", type="json")
    def contact(self, **kwargs):
        data = {}
        data['request_received'] = kwargs
        contact = http.request.e
        nv['design.client'].sudo().create(kwargs)
        return data



# class Design(http.Controller):
#     @http.route('/design/design/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/design/design/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('design.listing', {
#             'root': '/design/design',
#             'objects': http.request.env['design.design'].search([]),
#         })

#     @http.route('/design/design/objects/<model("design.design"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('design.object', {
#             'object': obj
#         })
