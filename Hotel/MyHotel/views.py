from django.http import HttpResponse
from django.shortcuts import render
from .models import RoomTypes, Customers


def index(request):
    return render(request, 'MyHotel/ButtonsForQueries.html', {})


def roomTypes(request):
    data = RoomTypes.objects.all()
    return render(request, 'MyHotel/QueriesResults.html', {"code": data})


def customers(request):
    data = Customers.objects.all()
    return render(request, 'MyHotel/QueriesResults.html', {"code1": data})