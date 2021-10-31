# -*- coding: utf-8 -*-

from odoo import models, fields, api


class student(models.Model):
     _name = 'school.student'#define el nombre del modelo
     _description = 'school.student'

     name = fields.Char(string="Nom", readonly=False, required=True, help='Este es el nombre')
     birth_year = fields.Integer()
     description = fields.Text()
     enrollment_date = fields.Date()
     last_login = fields.Datetime()
     is_student = fields.Boolean()
     #photo = fields.Binary()
     photo = fields.Image(max_width=200, max_height=200)
     classroom = fields.Many2one('school.classroom', ondelete='set null', help='La clase a la que va')
     teachers = fields.Many2many('school.teacher', related='classroom.teachers', readonly=True)#no se guarda en BD pero queremos mostrarlo

class classroom(models.Model):
     _name= 'school.classroom'
     _description = 'Las clases'

     name = fields.Char()
     students = fields.One2many(comodel_name='school.student', inverse_name='classroom')#no se guarda en BD, pero permite consultar info
     teachers = fields.Many2many(comodel_name='school.teacher', 
                                   relation='teachers_classroom', 
                                   column1='classroom_id',
                                   column2='teacher_id')
     

class teacher(models.Model):
     _name= 'school.teacher'
     _description = 'Los profesores'

     name = fields.Char()
     classrooms = fields.Many2many('school.classroom',
                                   relation='teachers_classroom', 
                                   column2='classroom_id',
                                   column1='teacher_id')

