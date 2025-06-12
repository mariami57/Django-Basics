from django import forms

from trip.models import Trip


class TripBaseForm(forms.ModelForm):
    class Meta:
        model = Trip
        exclude = ('traveler',)
        ordering = ('-start_date',)


class TripCreateForm(TripBaseForm):
    pass

class TripEditForm(TripBaseForm):
    pass


class TripDeleteForm(TripBaseForm):
    pass
