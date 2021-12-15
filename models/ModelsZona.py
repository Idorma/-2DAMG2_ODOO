# -*- coding: utf-8 -*-

from odoo import api
from odoo import fields
from odoo import models

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
    _name = 'lauserri.zona'

    nombreZona = fields.String()
    fechaCreacionZona = fields.Date()
    granja = fields.Many2One('lauserri.granja')
    animales = fields.One2Many('lauserri.animal','zona', string="Animales por zona")
    trabajadores = fields.Many2Many('lauserri.trabajador', string="Trabajadores por zona")