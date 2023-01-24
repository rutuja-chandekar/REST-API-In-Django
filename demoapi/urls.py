from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('item/', views.get_data, name='item'),
    path('add/', views.addItem, name= 'addItem'),
    path('delete/', views.deleteItem, name= 'deleteItem'),
    path('update/', views.updateItem, name= 'updateItem'),
]
