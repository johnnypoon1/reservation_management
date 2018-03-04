from __future__ import unicode_literals

from django.db import models


RESERVATION_STATUS = (
    ('reserved', "Reserved"),
    ('cancelled', "Cancelled"),
    ('Checked in', "Checked in"),
    ('Checked out', "Checked out"),
    ('help', "Requesting Services"))

class BedType(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    width = models.FloatField()
    length = models.FloatField()

    def __str__(self):
        return self.name


class RoomType(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200, blank=True, null=True)
    price = models.FloatField()
    bed_type = models.ForeignKey(BedType)
    number_beds = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name


class Room(models.Model):
    floor = models.IntegerField(default=0, blank=True, null=True)
    room_num = models.CharField(max_length=200)
    room_type = models.ForeignKey(RoomType)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.room_num


class Reservation(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=20)
    arrival = models.DateField(auto_now=False)
    departure = models.DateField(auto_now=False)
    status = models.CharField(max_length=20, default='reserved', choices=RESERVATION_STATUS)
    last_modified = models.DateTimeField(auto_now=True)
