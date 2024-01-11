import logging
import random
import time
from odoo import models, fields, api

class Override(models.Model):
    _name = "test_overideaddon.override"
    _description = "Override testing"
    
    @api.model
    def override_test(self):
        print('############################')