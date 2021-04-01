from django.urls import path
from . import views




urlpatterns = [
    path('<int:pk>/', views.dish_detail, name='dish_detail'),
    path('new', views.dish_new, name='dish_new'),
    path('<int:pk>/edit/', views.dish_edit, name='dish_edit'),
    path('<int:pk>/delete/', views.dish_delete),  

]
