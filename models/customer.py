from odoo import models, fields


class BusinessCustomer(models.Model):
    _name = 'business.customer'
    _description = 'Business Customer'

    name = fields.Char(string="Customer Name", required=True)
    contact_number = fields.Char(string="Contact Number")
    email = fields.Char(string="Email")
    address = fields.Text(string="Address")
    nic_br_number = fields.Char(string="NIC / BR Number")

    customer_type = fields.Selection([
        ('individual', 'Individual'),
        ('business', 'Business')
    ], string="Customer Type", default='individual')