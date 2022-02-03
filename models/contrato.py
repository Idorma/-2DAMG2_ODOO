# -*- coding: utf-8 -*-

from odoo import api
from odoo import exceptions
from odoo import fields
from odoo import models

class Contrato(models.Model):
    _name = 'lauserri.contrato'
    trabajador = fields.Many2one('lauserri.trabajador')
    granja = fields.Many2one('lauserri.granja')
    fechaContratacion = fields.Date()
    salario = fields.Integer()
    
    @api.constrains('salario')
    def _validar_salario_positivo(self):
        if self.salario < 0:
            raise exceptions.ValidationError("Salario no puede ser negativo")
    
    @api.constrains('fechaContratacion')
    def _validar_fecha_antes_hoy(self):
        
        if self.fechaContratacion > fields.Date.today():
            raise exceptions.ValidationError("Fecha no puede ser despues de la actual")
        
    @api.onchange('salario')
    def _control_salario(self):
        if self.salario < 0:
            raise exceptions.ValidationError("Salario no puede ser negativo")
  