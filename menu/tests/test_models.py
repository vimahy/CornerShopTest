from django.db import models
from django.test import TestCase
from menu.models import Menu
from django.utils import timezone


class TestModels(TestCase):


    def create_menu(self, name="Menu for today",date=timezone.localtime(), created_at= timezone.localtime()):
        return Menu.objects.create(name=name, date=date, created_at=created_at)

        
    def test_create_menu(self):
        """Checks if menu was correctly created"""
        menu = self.create_menu()
        self.assertTrue(isinstance(menu, Menu))
        self.assertIsNotNone(menu.unique_id)

