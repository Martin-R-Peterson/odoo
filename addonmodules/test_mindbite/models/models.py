

from odoo import models, fields, api, http
import requests


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

    def add_data_to_db(self, listActivities):
        for activity in listActivities:
            self.create(activity)
        
    def call_api(self):
        result = requests.env['ir.http'].dispatch_rpc('/test_mindbite/fetch_items', {})
        return True 

    def createtodo(self):
        todo_task_obj = self.env['todo.task']
        for activity in self:
            todo_task_obj.create({
                'name': activity.name,
                'description': f"Type: {activity.activity_type}\nParticipants: {activity.participants}\nPrice: {activity.price}\nLink: {activity.link}\nAccessibility: {activity.accessibility}",
            })
    
    def print(self):
        print("HEJHEJHEJ")

