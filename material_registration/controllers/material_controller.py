from odoo import http
from odoo.http import request


class MaterialWebController(http.Controller):

    @http.route('/materials', auth='public', website=True)
    def list_materials(self, **kwargs):
        """Menampilkan semua material di halaman web."""
        materials = request.env['material.registration'].sudo().search([])
        return request.render('material_registration.materials_list', {
            'materials': materials
        })

    @http.route('/materials/create', auth='public', website=True, methods=['GET', 'POST'], csrf=False)
    def create_material(self, **post):
        """Membuat material baru dari tampilan web."""
        if request.httprequest.method == 'POST':
            if float(post.get('material_buy_price', 0)) < 100:
                return request.render('material_registration.material_form', {'error': 'Harga beli minimal 100.'})

            request.env['material.registration'].sudo().create({
                'material_code': post.get('material_code'),
                'material_name': post.get('material_name'),
                'material_type': post.get('material_type'),
                'material_buy_price': post.get('material_buy_price'),
                'supplier_id': int(post.get('supplier_id')),
            })
            return request.redirect('/materials')
        suppliers = request.env['res.partner'].sudo().search([])
        return request.render('material_registration.material_form', {'suppliers': suppliers})

    @http.route('/materials/<int:material_id>/update', auth='public', website=True, methods=['GET', 'POST'], csrf=False)
    def update_material(self, material_id, **post):
        """Mengupdate material dari tampilan web."""
        material = request.env['material.registration'].sudo().browse(material_id)
        if request.httprequest.method == 'POST':
            material.write({
                'material_code': post.get('material_code'),
                'material_name': post.get('material_name'),
                'material_type': post.get('material_type'),
                'material_buy_price': post.get('material_buy_price'),
                'supplier_id': int(post.get('supplier_id')),
            })
            return request.redirect('/materials')
        suppliers = request.env['res.partner'].sudo().search([])
        return request.render('material_registration.material_form', {'material': material, 'suppliers': suppliers})

    @http.route('/materials/<int:material_id>/delete', auth='public', website=True, methods=['POST'], csrf=False)
    def delete_material(self, material_id, **kwargs):
        """Menghapus material dari tampilan web."""
        material = request.env['material.registration'].sudo().browse(material_id)
        if material.exists():
            material.unlink()
        return request.redirect('/materials')