from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    parent_l10n_mx_edi_addenda = fields.Many2one(related="parent_id.l10n_mx_edi_addenda")
    nombre_addenda = fields.Selection(string="Nombre de Addenda", selection=[('femsa', 'Femsa'), ('soriana', 'Soriana'), ])
    #femsa
    num_proovedor = fields.Char(string="No. de Proovedor", copy=False)
    # #soriana
    shipping_number_provider = fields.Char(string="No. de Proovedor", copy=False)
    shipping_number_store = fields.Integer(string="No. de Tienda", copy=False)
    shipping_number_cedis = fields.Integer(string="No. de Cedis", copy=False)