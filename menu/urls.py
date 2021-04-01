from django.urls import path
from . import views




urlpatterns = [
    path('', views.menu_list, name='menu_list'),
    path('<str:unique_id>', views.menu_detail, name='menu_detail'),
    path('new/', views.menu_new, name='menu_new'),
    path('<int:pk>/edit/', views.menu_edit, name='menu_edit'),
    path('<int:pk>/delete/', views.menu_delete),
    path('<int:pk>/send/', views.menu_send),  

]
