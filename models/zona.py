# -*- coding: utf-8 -*-

from odoo import api
from odoo import fields
from odoo import models
from odoo import exceptions

# class lauserri(models.Model):
#     _name = 'lauserri.lauserri'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

class ZonaEntity(models.Model):
    _name = "lauserri.zona"
    nombreZona = fields.Char()
    fechaCreacionZona = fields.Date()
    granja = fields.Many2one('lauserri.granja')
    animales = fields.One2many('lauserri.animal','zona', string="Animales por zona")
    trabajadores = fields.Many2many('lauserri.trabajador', string="Trabajadores por zona")
    
    
    @api.constrains('fechaCreacionZona')
    def _validar_fecha_antes_actual(self):
        if self.fechaCreacionZona > fields.Date.today():
            raise exceptions.ValidationError("La fecha de creacion no puede ser posterior a la actual")
    
    @api.onchange('fechaCreacionZona')
    def _control_fecha_antes_actual(self):
        if self.fechaCreacionZona > fields.Date.today():
            raise exceptions.ValidationError("La fecha de creacion no puede ser posterior a la actual")
