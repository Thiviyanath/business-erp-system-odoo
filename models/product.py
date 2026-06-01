from odoo import models, fields, api


class BusinessProduct(models.Model):
    _name = 'business.product'
    _description = 'Business Product'

    name = fields.Char(string="Vehicle Name", required=True)
    product_code = fields.Char(string="Stock ID")
    category = fields.Char(string="Vehicle Type")

    buying_price = fields.Float(string="Buying Price")
    selling_price = fields.Float(string="Selling Price")

    stock_quantity = fields.Integer(string="Available Units")
    low_stock_limit = fields.Integer(string="Low Stock Alert", default=1)

    image = fields.Image(string="Vehicle Image")

    status = fields.Selection([
        ('available', 'Available'),
        ('low_stock', 'Low Stock'),
        ('sold_out', 'Sold Out')
    ], string="Status", compute="_compute_status", store=True)

    active = fields.Boolean(default=True)

    @api.depends('stock_quantity', 'low_stock_limit')
    def _compute_status(self):
        for record in self:
            if record.stock_quantity <= 0:
                record.status = 'sold_out'
            elif record.stock_quantity <= record.low_stock_limit:
                record.status = 'low_stock'
            else:
                record.status = 'available'