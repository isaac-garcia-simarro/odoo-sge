# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime, timedelta

class soci(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    valvules = fields.One2many(comodel_name='sumacarcer.valvula', 
                                inverse_name='soci')

class valvula(models.Model):
    _name = 'sumacarcer.valvula'
    _description = 'Valvules'

    name = fields.Char()
    cabal = fields.Float()
    soci = fields.Many2one('res.partner')
    
    servicis = fields.One2many(comodel_name='sumacarcer.servici', 
                                inverse_name='valvula')
     


class servici(models.Model):
    _name = 'sumacarcer.servici'
    _description = 'Servici'

    name = fields.Char()
    hora_inici = fields.Datetime()
    hora_fi = fields.Datetime()
    valvula = fields.Many2one('sumacarcer.valvula')
    
    total_m3 = fields.Float(compute='_get_total')


    def _get_total(self):
        for p in self:
            start=fields.Datetime.from_string(p.hora_inici)
            end=fields.Datetime.from_string(p.hora_fi)

            p.total_m3 = (end - start).total_seconds() * p.valvula.cabal


# class sumacarcer(models.Model):
#     _name = 'sumacarcer.sumacarcer'
#     _description = 'sumacarcer.sumacarcer'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
