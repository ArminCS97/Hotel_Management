from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name='index'),
    path('RoomTypes', views.roomTypes),
    path('Customers', views.customers),
    path('Query1', views.q1),
    path('Query2', views.q2),
    path('Query3', views.q3),
    path('Query4', views.q4),
]