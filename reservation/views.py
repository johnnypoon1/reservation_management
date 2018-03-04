from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from django.utils import timezone

from apps import ReservationConfig as config
from reservation.forms import RoomBookingForm
from reservation.models import *
import datetime



def traffic_control(request, reservation_id=None):
    try:
        last_action = Reservation.objects.get(id=reservation_id).last_modified

        # if last action is taken less than 30 seconds ago
        if (timezone.now() - last_action).total_seconds() < config.request_rate:
            return HttpResponse("Traffic control: You are taking actions too quick")
        else:
            return True
    except:
        HttpResponse("Error on handling your request")

def index(request):
    room_types = RoomType.objects.all()
    rooms = []
    for room in room_types:
        room_left = len(Room.objects.filter(room_type=room, available=True))
        rooms.append({'id': room.id, 'room_type': room.name, 'description': room.description, 'room_left': room_left,
                      'price': room.price})

    reservations = Reservation.objects.all()  # List out all the reservation data
    return render(request, 'index.html', {'available_rooms': rooms, 'reservations': reservations})

def room_detail(request, room_type_id):
    try:
        room = RoomType.objects.get(id=room_type_id)
        room_left = len(Room.objects.filter(room_type=room, available=True))
        return render(request, 'room_detail.html', {'room': room, 'room_left': room_left})
    except ObjectDoesNotExist:
        return HttpResponse("Error loading this room")


def reserve(request, room_type_id):
    if request.method == "POST":  # if it is a form submit request
        form = RoomBookingForm(request.POST)
        if form.is_valid():
            # Get a list of available rooms for the same room type
            rooms = Room.objects.filter(room_type__id=room_type_id, available=True)
            if len(rooms) <= 0:  # checking room availability again
                return HttpResponse("This room is no longer available.")
            else:
                data = form.save(commit=False)
                rooms[0].available = False
                rooms[0].save()
                data.room = rooms[0]
                data.save()
                return HttpResponseRedirect(reverse('index'))
    else:
        form = RoomBookingForm(initial={'arrival': datetime.datetime.today(), 'room_type': room_type_id})

    return render(request, 'reserve_page.html', {'form': form, 'room_type_id': room_type_id})

def remove(request, reservation_id):
    stop = traffic_control(request, reservation_id=reservation_id)
    if stop is not True:
        return stop
    try:
        reservation = Reservation.objects.get(id=int(reservation_id))
        reservation.status = 'cancelled'
        reservation.last_modified = timezone.now()
        reservation.save()

        # Set room to be available again
        reservation.room.available = True
        reservation.room.save()
    except ObjectDoesNotExist, ValueError:
        return HttpResponse("Error occurred when handling your check in process.")
    return HttpResponseRedirect(reverse('index'))

def checkin(request, reservation_id):
    stop = traffic_control(request, reservation_id=reservation_id)
    if stop is not True:
        return stop
    try:
        reservation = Reservation.objects.get(id=int(reservation_id))
        reservation.status = 'Checked in'
        reservation.last_modified = timezone.now()
        reservation.save()
    except ObjectDoesNotExist, ValueError:
        return HttpResponse("Error occurred when handling your check in process.")
    return HttpResponseRedirect(reverse('index'))

def checkout(request, reservation_id):
    stop = traffic_control(request, reservation_id=reservation_id)
    if stop is not True:
        return stop
    try:
        reservation = Reservation.objects.get(id=int(reservation_id))
        reservation.status = 'Checked out'
        reservation.last_modified = timezone.now()
        reservation.save()

        # Set room to be available again
        reservation.room.available = True
        reservation.room.save()
    except ObjectDoesNotExist, ValueError:
        return HttpResponse("Error occurred when handling your check out process.")
    return HttpResponseRedirect(reverse('index'))
