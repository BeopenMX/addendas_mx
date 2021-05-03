from odoo import fields, models,api
CFDI_TEMPLATE_33 = 'l10n_mx_edi.cfdiv33'

class AccountMove(models.Model):
    _inherit = 'account.move'

    nombre_addenda = fields.Selection(string='Nombre de Addenda', related="partner_id.nombre_addenda")
    #FEMSA
    num_sociedad = fields.Char(string="No. de sociedad", copy=False)
    num_remision = fields.Char(string="No. de Remisión", copy=False)
    num_entrada = fields.Char(string="No. de Entrada", copy=False)

    #SORIANA
    tipo_bulto = fields.Selection(string="Tipo de Bulto",
                                  selection=[('1', 'Cajas'), ('2', 'Bolsa'), ], required=False, )
    date_of_deli = fields.Date(string="Fecha Entrega Mercancia", copy=False)
    cita = fields.Char(string="Folio de cita", copy=False)

    def try_addenda(self):
        qweb = self.env['ir.qweb']
        values = self._l10n_mx_edi_create_cfdi_values()
        cfdi = qweb.render(CFDI_TEMPLATE_33, values=values)
        return cfdi