from django.urls import path
from menu_app import views

urlpatterns = [
    path('', views.menu_list, name='menu_list'),
    path('additem/', views.add_item, name='add_item')
]