from django.contrib import admin

from .models import (Banquets, Bills, Booking, RoomFeedback,
                     SecuritySchedule, Customers, Rooms,
                     Reservations, RoomTypes, Payouts, Employees,
                     Guests)


@admin.register(Banquets, Bills, Booking, RoomFeedback,
                Customers, Rooms,
                Reservations, RoomTypes, Payouts,
                Guests)
class GuestAdmin(admin.ModelAdmin):
    pass


@admin.register(SecuritySchedule, Employees,
                )
class HotelAdmin(admin.ModelAdmin):
    pass

