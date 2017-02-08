# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class Product_Encoparts(models.Model):
    _inherit = 'product.template'

    Alternate_name = fields.Char('Alternate Name')
    ProductURL = fields.Char('Product URL')
    Detail = fields.Text('Detail')


 