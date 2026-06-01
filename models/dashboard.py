from odoo import models, fields, api


class BusinessDashboard(models.Model):
    _name = 'business.dashboard'
    _description = 'Business Dashboard'

    name = fields.Char(default="Dashboard")

    total_products = fields.Integer(
        string="Total Vehicles",
        compute='_compute_dashboard'
    )

    total_customers = fields.Integer(
        string="Total Customers",
        compute='_compute_dashboard'
    )

    total_sales = fields.Integer(
        string="Total Sales",
        compute='_compute_dashboard'
    )

    total_profit = fields.Float(
        string="Total Profit",
        compute='_compute_dashboard'
    )

    @api.depends()
    def _compute_dashboard(self):

        products = self.env['business.product'].search([])
        customers = self.env['business.customer'].search([])
        sales = self.env['vehicle.sales'].search([])

        for record in self:

            record.total_products = len(products)
            record.total_customers = len(customers)
            record.total_sales = len(sales)

            total_profit = 0

            for sale in sales:
                total_profit += sale.profit

            record.total_profit = total_profit