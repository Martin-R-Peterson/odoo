

from odoo import models, fields, api


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
        response = requests.get('your_api_endpoint', params={'limit': 10})

        if response.status_code == 200:
            data = response.json() 

            for item in data:
                self.create({
                    'name': item.get('activity'), 
                    'activity': item.get('activity'),
                    'activity_type': item.get('type'),
                    'participants': item.get('participants'),
                    'price': item.get('price'),
                    'link': item.get('link'),
                    'accessibility': item.get('accessibility'),
                })
        else:
            pass

