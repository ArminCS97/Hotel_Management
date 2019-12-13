from collections import Iterable

from django.db import models


# Django creates an auto incremented Id for each model but here just for the
# sake of emphasis I created id for each model explicitly


class Banquets(models.Model):
    id = models.AutoField(primary_key=True)
    breakfast = models.IntegerField(null=False, help_text="Breakfast", blank=False)
    dinner = models.IntegerField(null=False, help_text="Dinner", blank=False)
    supper = models.IntegerField(null=False, help_text="Supper", blank=False)
    all_inclusive = models.IntegerField(null=False, help_text="all_inclusive", blank=False)
    price = models.DecimalField(null=True, max_digits=5, decimal_places=2)

    def __str__(self):
        return str(self.id) + " | " + str(self.__class__)


class Bills(models.Model):
    id = models.AutoField(primary_key=True)
    reason = models.CharField(max_length=255, null=False, default="", blank=True)
    amount = models.DecimalField(null=False, max_digits=5, decimal_places=2, blank=False)
    date = models.DateField(auto_now=True, null=False, blank=False)


class Customers(models.Model):
    SSN = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False, blank=False)
    surname = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, null=False, unique=True)
    date_of_birth = models.DateField(auto_now_add=True, null=False)
    gender = models.CharField(max_length=255, null=True, blank=True)


class Employees(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False, blank=False)
    surname = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, null=False, unique=True)
    date_of_birth = models.DateField(auto_now_add=True, null=False)
    position = models.CharField(max_length=255, null=True, blank=True)


class RoomTypes(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=30, null=True, blank=False)
    price = models.DecimalField(null=True, max_digits=5, decimal_places=2)

    def __dir__(self):
        return ['id', 'type', 'price']


class Rooms(models.Model):
    number = models.AutoField(primary_key=True)
    type_id = models.ForeignKey(RoomTypes, on_delete=models.CASCADE)
    floor = models.PositiveIntegerField(null=True)


class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    customer_SSN = models.ForeignKey(Customers, on_delete=models.CASCADE)
    employee_id = models.ForeignKey(Employees, on_delete=models.CASCADE)
    room_number = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    check_in = models.DateTimeField(null=False, auto_now_add=True)
    check_out = models.DateTimeField(null=False, auto_now_add=True)


class Guests(models.Model):
    id = models.AutoField(primary_key=True)
    room_number = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False, blank=False)
    surname = models.CharField(max_length=255, null=True, blank=True)
    come_time = models.DateTimeField(null=False, auto_now_add=True)
    leave_time = models.DateTimeField(null=True, auto_now_add=True)


class Payouts(models.Model):
    id = models.AutoField(primary_key=True)
    bill_id = models.ForeignKey(Bills, on_delete=models.CASCADE)
    amount = models.DecimalField(null=False, max_digits=5, decimal_places=2)
    currency = models.CharField(max_length=255, null=False, default='USD')
    date = models.DateTimeField(null=False, auto_now_add=True)


class Reservations(models.Model):
    id = models.AutoField(primary_key=True)
    room_number = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    customer_SSN = models.ForeignKey(Customers, on_delete=models.CASCADE)
    bill_id = models.ForeignKey(Bills, on_delete=models.CASCADE)
    banquet_id = models.ForeignKey(Banquets, on_delete=models.CASCADE)
    date_from = models.DateTimeField(null=False, auto_now_add=True)
    date_until = models.DateTimeField(null=False, auto_now_add=True)


class RoomFeedback(models.Model):
    id = models.AutoField(primary_key=True)
    room_number = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    starts = models.IntegerField(default=5, null=False)
    comment = models.TextField(null=True, blank=True)


class SecuritySchedule(models.Model):
    id = models.AutoField(primary_key=True)
    employee_id = models.ForeignKey(Employees, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=255, null=True)
    time_start = models.DateTimeField(null=True)
    time_end = models.DateTimeField(null=True)
