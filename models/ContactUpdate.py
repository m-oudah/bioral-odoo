# -*- coding: utf-8 -*-
from odoo import models, fields, api
#
class ContactUpdate(models.Model):
    _inherit = 'res.partner'
    bioralcustomer = fields.Boolean(string='Is Customer')
    bioralvendor = fields.Boolean(string='Is Vendor')


    # channel_ids = fields.Many2many('mail.channel','mail_channel_profile_partner', 'partner_id', 'channel_id', copy=False)

    # partner_id = fields.Many2one(
    #     comodel_name="res.partner",
    #     string="Partner",
    #     required=True,
    #     index=True,
    #     auto_join=True,
    #     delegate=True,
    #     ondelete="restrict",
    # )