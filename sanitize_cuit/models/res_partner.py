from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    vat = fields.Char(string='VAT')

    @api.model
    def create(self, vals):
        if 'vat' in vals and isinstance(vals['vat'], str):
            vals['vat'] = vals['vat'].replace('-', '').replace('.', '')
        return super(ResPartner, self).create(vals)

    def write(self, vals):
        if 'vat' in vals and isinstance(vals['vat'], str):
            vals['vat'] = vals['vat'].replace('-', '').replace('.', '')
        return super(ResPartner, self).write(vals)
