from django.db import models
from django.test import TestCase
from dishes.models import Dish
from menu.models import Menu
from django.utils import timezone



class TestModels(TestCase):

    def setUp(self):
        self.menu =Menu.objects.create(date=timezone.localtime(), name="test" ,created_at=timezone.localtime())
        
    def create_dish(self):
        dish = Dish.objects.create(name="test", created_at=timezone.localtime(), menu=self.menu)
        
    def test_create_dish(self):
        """Checks if menu was correctly created"""
        dish = self.create_dish()
        

