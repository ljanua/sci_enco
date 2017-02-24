# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models
from datetime import date, timedelta, datetime
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT
from dateutil.relativedelta import relativedelta



class Sale_Encoparts(models.Model):
    _inherit = 'sale.order'
    _description = 'Adding 30 days for the validity_date and setting it as default'
    
    def _getDatePlus30Days(self):
        today = fields.Date.context_today(self)
        datetime_today = fields.Datetime.from_string(today)
        return datetime_today + relativedelta(days=+30)
           
    validity_date = fields.Date(string='Expiration Date', readonly=True, states={'draft': [('readonly', False)], 'sent': [('readonly', False)]},
        help="Manually set the expiration date of your quotation (offer), or it will set the date automatically based on the template if online quotation.", default=_getDatePlus30Days)
    



 