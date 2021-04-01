from django.db import models
from django.test import TestCase
from user.models import User
from django.utils import timezone


class TestModels(TestCase):


    def create_user(self,
                   email="test@gmail.com",
                   password='password',
                   first_name="first",
                   last_name="last",
                   ):
                   
                   
        return User.objects.create(email=email, 
                                  password=password, 
                                  first_name=first_name,
                                  last_name=last_name)

        
    def test_create_user(self):
        """Checks if dorder was correctly created"""
        user = self.create_user()
        self.assertTrue(isinstance(user, User))

