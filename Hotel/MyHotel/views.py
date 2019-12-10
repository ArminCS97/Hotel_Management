from django.http import HttpResponse
from django.shortcuts import render
from .models import RoomTypes, Customers


def index(request):
    return render(request, 'MyHotel/ButtonsForQueries.html', {})


def roomTypes(request):
    return render(request, 'MyHotel/QueriesResults.html', {"code": RoomTypes.objects.all()})


def customers(request):
    return render(request, 'MyHotel/QueriesResults.html', {"code1": Customers.objects.all()})