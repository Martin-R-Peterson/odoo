from odoo import http
from odoo.http import request


class OverrideAddon(http.Controller):
    def index(self):
        print('Hello')