# -*- coding: utf-8 -*-

from odoo import models, fields, api

class GranjaEntity(models.Model):
      _name = 'lauserri.granja'
      nombreGranja = fields.Char()
      fechaCreacion = fields.Date()
      granjero = fields.Many2one('lauserri.granjero', string="Granja del granjero")
      zonas = fields.One2many('lauserri.zona', 'granja', string="Zonas de la granja")
      contratos = fields.One2many('lauserri.contrato', 'granja', string="Contratos de la granja")
