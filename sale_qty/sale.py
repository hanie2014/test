from osv import fields, osv

from tools.translate import _

class sale_order_line(osv.osv):

	_name = 'sale.order.line'
	_inherit = 'sale.order.line'

	def _set_qty(self, cr, uid, ids, field_name, arg, context=None):

		res = {}
		for line in self.browse(cr, uid, ids, context=context):


		return {'value': res, 'warning': {}}

	_columns = [
		'qty_pak': fields.function(_set_qty, string='Quantity'),
	]

sale_order_line()