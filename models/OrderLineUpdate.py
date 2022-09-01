# -*- coding: utf-8 -*-
from odoo import models, fields, api

class OrderLineUpdate(models.Model):
    _inherit = 'sale.order.line'
    size = fields.Char('size')
    size = fields.Char(string='Package', store=False ,related='product_id.product_tmpl_id.pack', readonly=False)



    # rel_company_selection = fields.Many2one('account.analytic.account', string="Company",
    #                                         related='rel_account_invoice.company_selection')
