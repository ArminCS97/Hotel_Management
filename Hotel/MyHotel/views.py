from django.db.models.functions import datetime
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from .models import RoomTypes, Customers, Reservations, Guests, RoomFeedback, Rooms



def index(request):
    return render(request, 'MyHotel/ButtonsForQueries.html', {})


def roomTypes(request):
    data = RoomTypes.objects.all()
    if not data:
        raise Http404
    return render(request, 'MyHotel/QueriesResults.html', {"code": data})


def customers(request):
    data = Customers.objects.filter(name__startswith='C').exclude(surname=None)
    if not data:
        raise Http404
    return render(request, 'MyHotel/Customers.html', {"code1": data})


def q1(request):
    customer_ssn = Customers.objects.get(name="Customer1")
    reservations = Reservations.objects.filter(customer_SSN=customer_ssn)
    if not reservations:
        raise Http404
    return render(request, 'MyHotel/QueriesResults.html', {"reserved": reservations})


def q2(request):
    roomNum = Customers.objects.filter(name='Customer1')
    if not roomNum:
        raise Http404
    return render(request, 'MyHotel/Customers.html', {"code1": roomNum})


def q3(request):
    customer_ssn = Customers.objects.get(name="Customer1")
    reservations = Reservations.objects.filter(customer_SSN=customer_ssn)

    customer_ssn2 = Customers.objects.get(name="Customer2")
    reservations2 = Reservations.objects.filter(customer_SSN=customer_ssn2)

    temp = []
    for r in reservations:
        if r not in reservations2:
            temp.append(r)
    if not reservations:
        raise Http404
    return render(request, 'MyHotel/QueriesResults.html', {"reserved": temp})


def q4(request):
    type_id = RoomTypes.objects.get(type='Double')
    if not type_id:
        raise Http404
    guests = Guests.objects.filter(room_number__type_id=type_id)
    if not guests:
        raise Http404
    return render(request, 'MyHotel/QueriesResults.html', {"code2": guests})


def q5(request):
    guests = Guests.objects.filter(room_number__floor='2').exclude(come_time=datetime.datetime.now())
    if not guests:
        raise Http404
    return render(request, 'MyHotel/QueriesResults.html', {"code2": guests})


def q6(request):
    reservations = Reservations.objects.filter(room_number=2).filter(bill_id__reason=None)
    if not reservations:
        raise Http404('No Queries Exist for this request')
    return render(request, 'MyHotel/QueriesResults.html', {"reserved": reservations})
