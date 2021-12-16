# -*- coding: utf-8 -*-

from odoo import models, fields, api


class odoo578(models.Model):
    _name = 'odoo578.pelicula'
    _description = 'model pelicula'

    name = fields.Char('Titulo',required=True)
    fecha = fields.Char(String='Fecha',required=True )
    genero = fields.Char(String='Genero', required=True)
    descripcion = fields.Char(String='Descripcion', required=True)

#    @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
