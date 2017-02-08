# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class Contacts_Encoparts(models.Model):
    _inherit = 'res.partner'

    Tax_Id = fields.Char('Tax Id')
    


 