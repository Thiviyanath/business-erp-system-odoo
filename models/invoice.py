from odoo import models, fields, api


class BusinessInvoice(models.Model):
    _name = 'business.invoice'
    _description = 'Business Invoice'

    invoice_number = fields.Char(
        string="Invoice Number",
        required=True,
        copy=False,
        readonly=True,
        default='New'
    )

    sale_id = fields.Many2one(
        'vehicle.sales',
        string="Related Sale",
        required=True
    )

    customer_id = fields.Many2one(
        related='sale_id.customer_id',
        string="Customer",
        store=True
    )

    product_id = fields.Many2one(
        related='sale_id.product_id',
        string="Vehicle",
        store=True
    )

    subtotal = fields.Float(
        string="Subtotal",
        related='sale_id.sale_price',
        store=True
    )

    vat_rate = fields.Float(
        string="VAT Rate (%)",
        default=18
    )

    vat_amount = fields.Float(
        string="VAT Amount",
        compute="_compute_total",
        store=True
    )

    grand_total = fields.Float(
        string="Grand Total",
        compute="_compute_total",
        store=True
    )

    payment_status = fields.Selection([
        ('unpaid', 'Unpaid'),
        ('paid', 'Paid')
    ], string="Payment Status", default='unpaid')

    @api.depends('subtotal', 'vat_rate')
    def _compute_total(self):
        for record in self:
            record.vat_amount = record.subtotal * record.vat_rate / 100
            record.grand_total = record.subtotal + record.vat_amount

    @api.model
    def create(self, vals):

        if vals.get('invoice_number', 'New') == 'New':

            last_invoice = self.search([], order='id desc', limit=1)

            if last_invoice:
                last_number = int(last_invoice.invoice_number.replace('INV', ''))
                new_number = last_number + 1
            else:
                new_number = 1

            vals['invoice_number'] = f'INV{new_number:04d}'

        return super(BusinessInvoice, self).create(vals)

    def action_mark_paid(self):
        self.payment_status = 'paid'

    def action_mark_unpaid(self):
        self.payment_status = 'unpaid'

