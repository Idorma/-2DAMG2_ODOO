# -*- coding: utf-8 -*-

from odoo import models, fields, api

class GranjeroEntity(models.Model):
    _name = 'lauserri.granjero'
    _inherit = 'res.users'

    granjas = fields.One2Many('lauserri.granja', 'granjero', string="Granjas de granjero")


