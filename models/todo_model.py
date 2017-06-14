# -*- coding: utf-8 -*-

from odoo import models, fields, api

class TodoTask(models.Model):

    _name = 'todo.task'
    _description = 'To-do Task'

    name = fields.Char(string='Description', required=True)
    is_done = fields.Boolean(string='Done')
    active = fields.Boolean(string='Active?', default=True)

@api.multi
def do_toggle_done(self):
    for task in self:
        task.is_done = not task.is_done # En cada registro invierte su valor
    return True

@api.model
def do_clear_done(self):
    dones = self.search([('is_done','=',True)])
    dones.write({'active': False})
    return True
