from odoo import models, fields, api


class PRODCAT(models.Model):
    _inherit = 'sale.order.line'
    # product_categ_id = fields.Selection(related='product_id.product_tmpl_id.type', string='Category')
    product_categ_id = 555