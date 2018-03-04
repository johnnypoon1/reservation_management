from django.contrib import admin

from .models import BedType, Reservation, Room, RoomType


admin.site.register(BedType)
admin.site.register(RoomType)
admin.site.register(Room)
admin.site.register(Reservation)
