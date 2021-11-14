# -*- coding: utf-8 -*-

from odoo import models, fields, api
#from odoo import _
#from odoo.exceptions import Warning
import logging
import random

_logger = logging.getLogger(__name__)


class player(models.Model):
     _name = 'spaceships_invaders.player'
     _description = 'Players'

     name = fields.Char(required=True, default='player1')
     birth_date = fields.Date(required=True, default=lambda self: fields.Date.today())
     gender = fields.Char(required=True, default='M')
     enrollment_date = fields.Date(default=lambda self: fields.Date.today())
     last_login = fields.Datetime()
     gold = fields.Integer(required=True, default=100)
     rock = fields.Integer(required=True, default=300)
     metal = fields.Integer(required=True, default=200)
     planets = fields.One2many(comodel_name='spaceships_invaders.planet', 
                                inverse_name='player')
     spaceships = fields.One2many(comodel_name='spaceships_invaders.spaceship', 
                                inverse_name='player')

class spaceship(models.Model):
     _name = 'spaceships_invaders.spaceship'
     _description = 'Spaceships'

     name = fields.Char(required=True, default='Apolo')
     life = fields.Integer(required=True, default=100)
     is_on_planet = fields.Boolean(required=True, default=True)
     
     type = player = fields.Many2one('spaceships_invaders.spaceship_type', 
                                        ondelete='set null', 
                                        help='Tipo de la nave')
     player = fields.Many2one('spaceships_invaders.player', ondelete='set null', help='Jugador al que pertenece')
     
     

class spaceship_type(models.Model):
    _name = 'spaceships_invaders.spaceship_type'
    _description = 'Spaceship Types'

    name = fields.Char(required=True, default='crucero')
    gold_needed = fields.Integer(required=True, default=50)
    rock_needed = fields.Integer(required=True, default=100)
    metal_needed = fields.Integer(required=True, default=100)
    damage = fields.Integer(required=True, default=lambda self: random.randint(20,100), readonly=True)
    life = fields.Integer(required=True,  default=lambda self: random.randint(50,200), readonly=True)


class planet(models.Model):
     _name = 'spaceships_invaders.planet'
     _description = 'Planets'

     name = fields.Char(required=True, default='namek')
     life = fields.Integer(required=True, default=lambda self: random.randint(300,1000), readonly=True)
     quantity_gold_hour = fields.Integer(required=True, default=lambda s: s.life/100, readonly=True)
     quantity_rock_hour = fields.Integer(required=True, default=lambda s: s.life/10, readonly=True)
     quantity_metal_hour = fields.Integer(required=True, default=lambda s: s.life/50, readonly=True)

     player = fields.Many2one('spaceships_invaders.player', ondelete='set null', help='Jugador al que pertenece')

