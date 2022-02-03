# -*- coding: utf-8 -*-

from odoo import api
from odoo import exceptions
from odoo import fields
from odoo import models

class GranjaEntity(models.Model):
      _name = 'lauserri.granja'
      nombreGranja = fields.Char(string="Nombre de la granja")
      fechaCreacion = fields.Date(string="Fecha de creacion de la granja")
      granjero = fields.Many2one('lauserri.granjero', string="Granjero de la granja")
      zonas = fields.One2many('lauserri.zona', 'granja', string="Zonas de la granja")
      contratos = fields.One2many('lauserri.contrato', 'granja', string="Contratos de la granja")
      
    @api.constrains('fechaCreacion')
    def _validar_fecha_actual(self):
        if self.fechaCreacion > fields.Date.today():
            raise exceptions.ValidationError("La fecha de creacion no puede ser posterior a la actual")
        
    @api.onchange('fechaCreacion')
    def _control_fecha_actual(self):
        if self.fechaCreacion > fields.Date.today():
            raise exceptions.ValidationError("La fecha de creacion no puede ser posterior a la actual")