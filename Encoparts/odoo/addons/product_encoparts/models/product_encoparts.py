# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class Product_Encoparts(models.Model):
    _inherit = 'product.template'

    Alternate_name = fields.Char('Alternate Name')
    ProductURL = fields.Char('Product URL')
    Specification = fields.Text('Specification')
    description_compatible_models = fields.Text(
        'Compatible Model Description', translate=True,
        help="A description of the Product compatible Models. "
             "This description will be copied to every Sale Order, Delivery Order and Customer Invoice/Refund")


 