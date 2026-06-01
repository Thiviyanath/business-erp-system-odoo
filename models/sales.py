from odoo import models, fields, api
from odoo.exceptions import ValidationError


class VehicleSales(models.Model):
    _name = 'vehicle.sales'
    _description = 'Vehicle Sales'

    customer_id = fields.Many2one(
        'business.customer',
        string="Customer",
        required=True
    )

    product_id = fields.Many2one(
        'business.product',
        string="Vehicle",
        required=True
    )

    sale_date = fields.Date(
        string="Sale Date",
        default=fields.Date.today
    )

    sale_price = fields.Float(
        string="Sale Price"
    )

    buying_price = fields.Float(
        string="Buying Price",
        related='product_id.buying_price',
        store=True
    )

    profit = fields.Float(
        string="Profit",
        compute='_compute_profit',
        store=True
    )

    payment_status = fields.Selection([
        ('pending', 'Pending'),
        ('paid', 'Paid')
    ], string="Payment Status", default='pending')

    notes = fields.Text(string="Notes")

    @api.depends('sale_price', 'buying_price')
    def _compute_profit(self):
        for record in self:
            record.profit = record.sale_price - record.buying_price

    @api.model
    def create(self, vals):

        sale = super(VehicleSales, self).create(vals)

        product = sale.product_id

        if product.stock_quantity <= 0:
            raise ValidationError("Vehicle out of stock!")

        product.stock_quantity -= 1

        return sale