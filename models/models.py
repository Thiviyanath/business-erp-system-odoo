# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class business_erp_system(models.Model):
#     _name = 'business_erp_system.business_erp_system'
#     _description = 'business_erp_system.business_erp_system'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

