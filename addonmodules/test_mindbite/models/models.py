

from odoo import models, fields, api, http
from odoo.http import request


class test_mindbite(models.Model):
    _name = 'test_mindbite'
    _description = 'test_mindbite stuff'
    name = fields.Char()
    activity = fields.Char()
    activity_type = fields.Char()
    participants = fields.Integer()
    price = fields.Float()
    link = fields.Char()
    accessibility = fields.Float()

    @api.model
    def fetch_data_from_api(self):
        print("#########################################################")
        # for responsenr in range(10):
        #     response = request.get('https://www.boredapi.com/api/activity')
        #     if response.status_code == 200:
        #         data = response.json() 

        #         self.create({
        #                 'name': data.get('activity'), 
        #                 'activity': data.get('activity'),
        #                 'activity_type': data.get('type'),
        #                 'participants': data.get('participants'),
        #                 'price': data.get('price'),
        #                 'link': data.get('link'),
        #                 'accessibility': data.get('accessibility'),
        #             })
        #     else:
        #         pass
            
