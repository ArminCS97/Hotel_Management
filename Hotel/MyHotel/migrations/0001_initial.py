# Generated by Django 2.2.4 on 2019-12-09 09:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banquets',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('breakfast', models.IntegerField(help_text='Breakfast')),
                ('dinner', models.IntegerField(help_text='Dinner')),
                ('supper', models.IntegerField(help_text='Supper')),
                ('all_inclusive', models.IntegerField(help_text='all_inclusive')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bills',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('reason', models.CharField(blank=True, default='', max_length=255)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('SSN', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('surname', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('date_of_birth', models.DateField(auto_now_add=True)),
                ('gender', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('surname', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('date_of_birth', models.DateField(auto_now_add=True)),
                ('position', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RoomTypes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=30, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SecuritySchedule',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('day_of_week', models.CharField(max_length=255, null=True)),
                ('time_start', models.DateTimeField(null=True)),
                ('time_end', models.DateTimeField(null=True)),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyHotel.Employees')),
            ],
        ),
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('number', models.AutoField(primary_key=True, serialize=False)),
                ('floor', models.PositiveIntegerField(null=True)),
                ('type_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyHotel.RoomTypes')),
            ],
        ),
        migrations.CreateModel(
            name='RoomFeedback',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('starts', models.IntegerField(default=5)),
                ('comment', models.TextField(blank=True, null=True)),
                ('room_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyHotel.Rooms')),
            ],
        ),
        migrations.CreateModel(
            name='Reservations',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date_from', models.DateTimeField(auto_now_add=True)),
                ('date_until', models.DateTimeField(auto_now_add=True)),
                ('banquet_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyHotel.Banquets')),
                ('bill_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyHotel.Bills')),
                ('customer_SSN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyHotel.Customers')),
                ('room_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyHotel.Rooms')),
            ],
        ),
        migrations.CreateModel(
            name='PayoutS',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('currency', models.CharField(default='USD', max_length=255)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('bill_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyHotel.Bills')),
            ],
        ),
        migrations.CreateModel(
            name='Guests',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('surname', models.CharField(blank=True, max_length=255, null=True)),
                ('come_time', models.DateTimeField(auto_now_add=True)),
                ('leave_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('room_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyHotel.Rooms')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('check_in', models.DateTimeField(auto_now_add=True)),
                ('check_out', models.DateTimeField(auto_now_add=True)),
                ('customer_SSN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyHotel.Customers')),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyHotel.Employees')),
                ('room_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyHotel.Rooms')),
            ],
        ),
    ]