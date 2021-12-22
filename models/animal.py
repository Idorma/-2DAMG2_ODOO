# -*- coding: utf-8 -*-

from odoo import models, fields, api

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

class AnimalEntity(models.Model):
    _name = 'lauserri.animal'
    nombreAnimal = fields.String()
    tipo = fields.TipoAnimal()
    estado = fields.EstadoAnimal()
    fechaNacimiento = fields.Date()
    sexo = fields.SexoAnimal()
    zona = fields.Many2one('lauserri.zona')