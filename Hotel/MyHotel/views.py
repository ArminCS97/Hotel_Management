from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from .models import RoomTypes, Customers, Reservations, Guests, RoomFeedback, Rooms
from .forms import CustomersForm


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
    customer = Customers.objects.filter(name='Customer1')
    if not customer:
        raise Http404
    return render(request, 'MyHotel/Customers.html', {"code1": customer})


def q2(request):
    roomNum = Customers.objects.filter(name='Customer1')
    if not roomNum:
        raise Http404
    return render(request, 'MyHotel/Customers.html', {"code1": roomNum})


def q3(request):  # to do
    try:
        reservations = Reservations.objects.all()
        for r in reservations:
            ssn = r.customers_SSN
            count = Reservations.objects.count(customers_SSN=ssn)
            if count >= 0:
                reservations.exclude(r)
            return render(request, 'MyHotel/Customers.html', {"code1": reservations})
    except ObjectDoesNotExist:
        return HttpResponse('No One Was Found')


def q4(request):
    type_id = RoomTypes.objects.get(type='Double')
    if not type_id:
        raise Http404
    guests = Guests.objects.filter(room_number__type_id=type_id)
    if not guests:
        raise Http404
    return render(request, 'MyHotel/QueriesResults.html', {"code2": guests})

