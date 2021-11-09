# -*- coding: utf-8 -*-

from odoo import models, fields, api
#from odoo import _
#from odoo.exceptions import Warning
import logging

_logger = logging.getLogger(__name__)


class player(models.Model):
     _name = 'spaceships_invaders.player'
     _description = 'Players'

     name = fields.Char(required=True)
     birth_date = fields.Date(required=True)
     gender = fields.Char(required=True)
     enrollment_date = fields.Date()
     last_login = fields.Datetime()
     gold = fields.Integer(required=True)
     rock = fields.Integer(required=True)
     metal = fields.Integer(required=True)
     planets = fields.One2many(comodel_name='spaceships_invaders.planet', 
                                inverse_name='player')
     spaceships = fields.One2many(comodel_name='spaceships_invaders.spaceship', 
                                inverse_name='player')

     def _get_password(self):
          for student in self:
               student.password = "pass aleatorio"
               #raise Warning(_('Algo ha fallado'))#debugging
               _logger.debug('\033[94m'+str(student)+'\033[0m')#debugging

class spaceship(models.Model):
     _name = 'spaceships_invaders.spaceship'
     _description = 'Spaceships'

     name = fields.Char(required=True)
     life = fields.Integer(required=True)
     is_on_planet = fields.Boolean(required=True)
     type = player = fields.Many2one('spaceships_invaders.spaceship_type', 
                                        ondelete='set null', 
                                        help='Tipo de la nave')
     player = fields.Many2one('spaceships_invaders.player', ondelete='set null', help='Jugador al que pertenece')
     
     

class spaceship_type(models.Model):
    _name = 'spaceships_invaders.spaceship_type'
    _description = 'Spaceship Types'

    name = fields.Char(required=True)
    gold_needed = fields.Integer(required=True)
    rock_needed = fields.Integer(required=True)
    metal_needed = fields.Integer(required=True)
    damage = fields.Integer(required=True)
    life = fields.Integer(required=True)


class planet(models.Model):
     _name = 'spaceships_invaders.planet'
     _description = 'Planets'

     name = fields.Char(required=True)
     life = fields.Integer(required=True)
     quantity_gold_hour = fields.Integer(required=True)
     quantity_rock_hour = fields.Integer(required=True)
     quantity_metal_hour = fields.Integer(required=True)

     player = fields.Many2one('spaceships_invaders.player', ondelete='set null', help='Jugador al que pertenece')

