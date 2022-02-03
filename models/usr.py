# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Usr(models.Model):
    _name = 'lauserri.usr'
    
    name = fields.Char()
    login = fields.Char()
    email = fields.Char()
    username = fields.Char()
    password = fields.Char()