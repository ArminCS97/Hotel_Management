from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import RoomTypes, Customers, Reservations, Guests, RoomFeedback
from .forms import CustomersForm


def index(request):
    return render(request, 'MyHotel/ButtonsForQueries.html', {})


def roomTypes(request):
    data = RoomTypes.objects.all()
    return render(request, 'MyHotel/QueriesResults.html', {"code": data})


def customers(request):
    data = Customers.objects.all()
    return render(request, 'MyHotel/Customers.html', {"code1": data})


def q1(request):
    customer = Customers.objects.filter(name='Customer1')
    return render(request, 'MyHotel/Customers.html', {"code1": customer})


def q2(request):
    roomNum = Customers.objects.filter(name='Customer1')
    return render(request, 'MyHotel/Customers.html', {"code1": roomNum})


def q3(request): # to do
    try:
        reservations = Reservations.objects.all()
        empty = []
        for r in reservations:
            ssn = r.customers_SSN
            count = Reservations.objects.count(customers_SSN = ssn)
            if count >= 2 and r not in empty:
                empty.append(r)
            return render(request, 'MyHotel/Customers.html', {"code1": empty})
    except ObjectDoesNotExist:
        return HttpResponse('No One Was Found')



def q4(request): # to do
    guests = Guests.objects.filter(type_id__type = 'Double')
    render(request, 'MyHotel/QueriesResult.html', {"code2": guests})



# def q3(request):
#     # if request.method == 'POST':
#     form = CustomersForm(request.POST)
#     #     if form.is_valid():
#     #         return HttpResponseRedirect('/MyHotel/')
#     # else:
#     #     form = CustomersForm()
#     return render(request, 'MyHotel/Customers.html' , {'form': form} )