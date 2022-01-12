# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Contrato(models.Model):
    _name='lauserri.contrato'
    trabajador=fields.Many2one('lauserri.trabajador')
    granja=fields.Many2one('lauserri.granja')
    fechaContratacion=fields.Date()
    salario=fields.Integer   