# -*- coding: utf-8 -*-

from odoo import api
from odoo import exceptions
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

class AnimalEntity(models.Model):
    _name = 'lauserri.animal'
    nombreAnimal = fields.Char()
    tipo = fields.Selection([('a', 'TORO'),
                            ('b', 'BUEY'),
                            ('c', 'VACA'),
                            ('d', 'CABALLO'),
                            ('e', 'YEGUA'),
                            ('f', 'ASNO'),
                            ('g', 'MULA'),
                            ('h', 'GALLO'),
                            ('i', 'GALLINA'),
                            ('j', 'PAVO'),
                            ('k', 'OVEJA'),
                            ('l', 'CARNERO'),
                            ('m', 'CABRA'),
                            ('n', 'CERDO')], string='TipoAnimal')
    estado = fields.Selection([('a', 'SANO'),
                              ('b', 'MUERTO'),
                              ('c', 'ENFERMO'),
                              ('d', 'EMBARAZADO'),
                              ('e', 'VENDIDO'),
                              ], string='EstadoAnimal')
    fechaNacimiento = fields.Date()
    sexo = fields.Selection([('a', 'HEMBRA'),
                            ('b', 'MACHO')
                            ], string='SexoAnimal')
    zona = fields.Many2one('lauserri.zona')
    
    @api.constrains('fechaNacimiento')
    def _validar_fecha_actual(self):
        if self.fechaNacimiento > fields.Date.today():
            raise exceptions.ValidationError("La fecha de nacimiento no puede ser posterior a la actual")
        
    @api.onchange('fechaNacimiento')
    def _control_fecha_actual(self):
        if self.fechaNacimiento > fields.Date.today():
            raise exceptions.ValidationError("La fecha de nacimiento no puede ser posterior a la actual")
