# -*- coding: utf-8 -*-

from odoo import models, fields, api

class GranjeroEntity(models.Model):
    _name = 'lauserri.granjero'
    _inherit = 'lauserri.usr'
    
    granjas = fields.One2many('lauserri.granja', 'granjero', string="Granjas de granjero")