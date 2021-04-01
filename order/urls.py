from django.urls import path
from . import views




urlpatterns = [
    path('', views.order_list, name='order_list'),
    path('unavailable', views.order_unavailable, name='order_unavailable'),
    path('<int:pk>/', views.order_detail, name='order_detail'),
    path('new', views.order_new, name='order_new'),
    path('<int:pk>/edit/', views.order_edit, name='order_edit'),
    path('<int:pk>/delete/', views.order_delete),  

]
