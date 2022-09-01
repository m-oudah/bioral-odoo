# -*- coding: utf-8 -*-
from odoo import models, fields, api

class SaleOrderUpdate(models.Model):
    _inherit = 'sale.order'
    origin_country = fields.Char(string='Origin Country')
    ship_to = fields.Char(string='Destination Port')
    ship_fees = fields.Integer(string='Shipping Fees')
    # new_amount_total = ship_fees

    # custom_field = fields.Char(string='Custom Field')