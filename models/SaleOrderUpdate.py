# -*- coding: utf-8 -*-
from odoo import models, fields, api

class SaleOrderUpdate(models.Model):
    _inherit = 'sale.order'
    origin_country = fields.Char(string='Origin Country')
    ship_to = fields.Char(string='Destination Port')
    ourcompany = fields.Integer(string='Our Company')
    # new_amount_total = ship_fees

    # custom_field = fields.Char(string='Custom Field')