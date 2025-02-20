from odoo import models, fields, api, http
from odoo.http import request
from odoo.exceptions import ValidationError


class Material(models.Model):
    _name = 'material.registration'
    _description = 'Material Registration'

    material_code = fields.Char(string='Material Code', required=True, copy=False)
    material_name = fields.Char(string='Material Name', required=True)
    material_type = fields.Selection([
        ('fabric', 'Fabric'),
        ('jeans', 'Jeans'),
        ('cotton', 'Cotton')
    ], string='Material Type', required=True)
    material_buy_price = fields.Float(string='Material Buy Price', required=True)
    supplier_id = fields.Many2one(
        'res.partner',
        string='Related Supplier',
        required=True
    )

    _sql_constraints = [
        ('material_code_unique', 'unique(material_code)', 'Material Code harus unik!')
    ]

    @api.constrains('material_buy_price')
    def _check_buy_price(self):
        for record in self:
            if record.material_buy_price < 100:
                raise ValidationError('Material Buy Price tidak boleh kurang dari 100.')