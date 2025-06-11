from django import forms

from trip.models import Trip


class TripBaseForm(forms.ModelForm):
    class Meta:
        model = Trip
        exclude = ('traveler',)
