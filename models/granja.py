# -*- coding: utf-8 -*-

from odoo import models, fields, api

class GranjaEntity(models.Model):
      _name = 'lauserri.granja'
      nombreGranja = fields.Char()
      fechaCreacion = fields.Date()
      granjero = fields.Many2One('lauserri.granjero', string="Granja del granjero")
      zonas = fields.One2Many('lauserri.zona', 'granja', string="Zonas de la granja")
      contratos = fields.One2Many('lauserri.contrato', 'granja', string="Contratos de la granja")