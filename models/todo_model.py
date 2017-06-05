# -*- coding: utf-8 -*-

from odoo import models, fields

class TodoTask(models.Model):

    _name: 'todo.task'
    _description: 'To-do Task'

    name = fields.Char(string='Description', required= True)
    is_done = fields.Boolean(string='Done')
    active = fields.Boolean(string='Active?', default= True)