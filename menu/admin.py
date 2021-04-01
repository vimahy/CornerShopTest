from django.contrib import admin

# Register your models here.
#myapp/admin.py
from menu.models import Menu

admin.site.register(Menu)
