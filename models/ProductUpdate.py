# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ProductUpdate(models.Model):
    _inherit = 'product.template'
    pack = fields.Char(string='Pack Size')

