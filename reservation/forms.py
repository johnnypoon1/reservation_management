from django import forms
from reservation import models
import datetime


class RoomBookingForm(forms.ModelForm):
    room_type = forms.CharField(required=False, max_length=5, widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        super(RoomBookingForm, self).__init__(*args, **kwargs)
        try:
            self.fields['room_type'].initial = kwargs['initial']['room_type']
        except KeyError:
            pass

    def clean(self):
        try:
            cleaned_data = super(RoomBookingForm, self).clean()
            check_in = cleaned_data.get("arrival", None)
            check_out = cleaned_data.get("departure", None)
            room_type = int(cleaned_data.get("room_type", None))

            if check_in < datetime.date.today():  # validate the check in date
                raise forms.ValidationError("Arrival date cannot be earlier than today", "Invalid arrival date")
            if check_out <= check_in:  # validate the check out date
                raise forms.ValidationError("Departure date must be later than arrival date", "Invalid Departure date")

            # check room availability based on room type
            if len(models.Room.objects.filter(room_type__id=room_type, available=True)) <= 0:
                raise forms.ValidationError("This room is no longer available", "No vacancy")

        except AttributeError, ValueError:
            raise forms.ValidationError("Error occurred on validating data", "Validation error")

    class Meta:
        model = models.Reservation
        fields = '__all__'
        exclude = ['room', 'status', 'last_modified']
