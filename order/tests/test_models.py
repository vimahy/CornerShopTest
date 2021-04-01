from django.db import models
from django.test import TestCase
from django.utils import timezone

from menu.models import Menu
from order.models import Order
from dishes.models import Dish

class TestModels(TestCase):

    def setUp(self):
        self.menu =Menu.objects.create(date=timezone.localtime(), name="test" ,created_at=timezone.localtime())
        self.menu_dish = Dish.objects.create(name="Dish Name",created_at=timezone.localtime(),menu=self.menu)
        
        
    def create_order(self):
        order = Order.objects.create(comment="test", created_at=timezone.localtime(), dish=self.dish)
        
    def test_create_order(self):
        """Checks if dorder was correctly created"""
        order = self.create_order()

