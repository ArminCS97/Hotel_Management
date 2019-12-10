from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name='index'),
    path('RoomTypes', views.roomTypes),
    path('Customers', views.customers),
]