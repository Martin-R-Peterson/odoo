
from odoo import http
import requests

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
    
    @http.route('/test_mindbite/fetch_items', type='http', auth="user")
    def fetch_items_from_api(self):
        test_mindbite = http.request.env['test_mindbite']
        activityList = []
        for responsenr in range(10):
            response = requests.get('https://www.boredapi.com/api/activity')
            if response.status_code == 200:
                data = response.json() 

                activityObject = ({
                        'name': data.get('activity'), 
                        'activity': data.get('activity'),
                        'activity_type': data.get('type'),
                        'participants': data.get('participants'),
                        'price': data.get('price'),
                        'link': data.get('link'),
                        'accessibility': data.get('accessibility'),
                    })
                activityList.append(activityObject)
            else:
                pass
        test_mindbite.add_data_to_db(activityList)
        return http.request.redirect('/web#model=test_mindbite&view_type=list')

