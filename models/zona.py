# -*- coding: utf-8 -*-

from odoo import api
from odoo import fields
from odoo import models

class ZonaEntity(models.Model):
    _name = "lauserri.zona"
    nombreZona = fields.Char()
    fechaCreacionZona = fields.Date()
    granja = fields.Many2one('lauserri.granja')
    animales = fields.One2many('lauserri.animal','zona', string="Animales por zona")
    trabajadores = fields.Many2many('lauserri.trabajador', string="Trabajadores por zona")