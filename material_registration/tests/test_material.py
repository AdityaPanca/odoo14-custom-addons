from odoo.tests.common import TransactionCase, HttpCase


class TestMaterialRegistration(TransactionCase):

    def setUp(self, *args, **kwargs):
        super().setUp(*args, **kwargs)
        self.supplier = self.env['res.partner'].create({'name': 'Supplier Test', 'supplier_rank': 1})
        self.material_vals = {
            'material_code': 'MAT001',
            'material_name': 'Test Material',
            'material_type': 'fabric',
            'material_buy_price': 150.0,
            'supplier_id': self.supplier.id
        }

    def test_create_material(self):
        material = self.env['material.registration'].create(self.material_vals)
        self.assertEqual(material.material_code, 'MAT001')
        self.assertGreaterEqual(material.material_buy_price, 100)

    def test_material_price_validation(self):
        self.material_vals['material_buy_price'] = 50
        with self.assertRaises(Exception):
            self.env['material.registration'].create(self.material_vals)