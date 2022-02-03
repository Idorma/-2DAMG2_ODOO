# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Trabajador(models.Model):
    _name = 'lauserri.trabajador'
    _inherit = 'lauserri.usr'
    
    contratos = fields.One2many('lauserri.contrato','trabajador',string='Contratos del trabajador')
    zonas = fields.Many2many('lauserri.zona', string='Zonas del trabajador')