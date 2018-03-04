from __future__ import unicode_literals

from django.apps import AppConfig


class ReservationConfig(AppConfig):
    name = 'reservation'
    request_rate = 30  # Cannot make another request until 30sec
