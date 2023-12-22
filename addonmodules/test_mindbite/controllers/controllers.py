
from odoo import http


class TestMindbite(http.Controller):
    @http.route('/test_mindbite/test_mindbite', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/test_mindbite/test_mindbite/objects', auth='public')
    def list(self, **kw):
        return http.request.render('test_mindbite.listing', {
            'root': '/test_mindbite/test_mindbite',
            'objects': http.request.env['test_mindbite.test_mindbite'].search([]),
        })

    @http.route('/test_mindbite/test_mindbite/objects/<model("test_mindbite.test_mindbite"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('test_mindbite.object', {
            'object': obj
        })
    
    @http.route('/your_module/fetch_items', type='http', auth="user")
    def fetch_items_from_api(self):
        your_new_model = http.request.env['test_mindbite']
        your_new_model.fetch_data_from_api()
        return http.request.redirect('/web#model=test_mindbite&view_type=list')

