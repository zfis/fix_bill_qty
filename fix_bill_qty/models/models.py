# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from datetime import datetime
from dateutil.relativedelta import relativedelta

from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.osv import expression
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
from odoo.tools.float_utils import float_compare
from odoo.exceptions import AccessError, UserError, ValidationError
from odoo.tools.misc import formatLang, get_lang


class PurchaseOrderLineInherits(models.Model):
	_inherit = "purchase.order.line"


	def _prepare_account_move_line(self, move):
		res = super(PurchaseOrderLineInherits, self)._prepare_account_move_line(move)
		if self.product_id.purchase_method == 'purchase':
			qty = self.product_qty - self.qty_invoiced
		else:
			qty = self.product_qty - self.qty_invoiced
		if float_compare(qty, 0.0, precision_rounding=self.product_uom.rounding) <= 0:
			qty = self.product_qty
		res['quantity'] = qty
		return res


	# def _prepare_account_move_line(self, move):
	# 	self.ensure_one()
	# 	if self.product_id.purchase_method == 'purchase':
	# 		qty = self.product_qty - self.qty_invoiced
	# 	else:
	# 		qty = self.qty_received - self.qty_invoiced
	# 	if float_compare(qty, 0.0, precision_rounding=self.product_uom.rounding) <= 0:
	# 		qty = self.product_qty
	# 	if self.currency_id == move.company_id.currency_id:
	# 		currency = False
	# 	else:
	# 		currency = move.currency_id
	# 	return {
	# 		'name': '%s: %s' % (self.order_id.name, self.name),
	# 		'move_id': move.id,
	# 		'currency_id': currency and currency.id or False,
	# 		'purchase_line_id': self.id,
	# 		'date_maturity': move.invoice_date_due,
	# 		'product_uom_id': self.product_uom.id,
	# 		'product_id': self.product_id.id,
	# 		'price_unit': self.price_unit,
	# 		'quantity': qty,
	# 		'partner_id': move.partner_id.id,
	# 		'analytic_account_id': self.account_analytic_id.id,
	# 		'analytic_tag_ids': [(6, 0, self.analytic_tag_ids.ids)],
	# 		'tax_ids': [(6, 0, self.taxes_id.ids)],
	# 		'display_type': self.display_type,
	# 	}
