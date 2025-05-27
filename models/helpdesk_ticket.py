from odoo.addons.helpdesk_repair.models.helpdesk_ticket import HelpdeskTicket




def _prepare_repairs_default_value(self):
        return {
            **self.env.context,
            'default_product_id': self.product_id.id,
            'default_lot_id': self.lot_id.id,
            'default_partner_id': self.partner_id.id,
            'default_ticket_id': self.id,
            'default_company_id': self.company_id.id,
            'default_description': self.name,
            'default_sale_order_id': self.user_has_groups('sales_team.group_sale_salesman,account.group_account_invoice')
                                      and self.sale_order_id.id or False,
            'default_user_id': False,
            'default_team_id': False,
            'default_internal_notes': self.description,
            'default_repair_picking_id': self.picking_ids.filtered(lambda x: x.product_id == self.product_id)[-1].id
                if self.picking_ids and self.product_id else self.picking_ids[-1:].id,
        }
HelpdeskTicket._prepare_repairs_default_value = _prepare_repairs_default_value