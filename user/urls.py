#Django imports
from django.urls import path

# View
from .import views

urlpatterns = [
   
    path('login/', views.auth_login, name='login'),
    path('logout/', views.auth_logout, name='logout'),
]
