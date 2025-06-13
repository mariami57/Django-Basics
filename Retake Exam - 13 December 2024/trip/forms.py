from django import forms

from trip.models import Trip


class TripBaseForm(forms.ModelForm):
    class Meta:
        model = Trip
        exclude = ("traveler",)
        ordering = ("-start_date",)
        help_texts = {
            "duration":"*Duration in days is expected.",
        }


class TripCreateForm(TripBaseForm):
    class Meta(TripBaseForm.Meta):
        widgets = {
            "destination": forms.TextInput(attrs={"placeholder": "Enter a short destination note..."}),
            "summary":forms.TextInput(attrs={"placeholder": "Share your exciting moments... "}),
            "start_date":forms.DateInput(attrs={"type":"date", }),
            "duration":forms.TextInput(),
            "image_url":forms.TextInput(attrs={"placeholder": "An optional image URL..."}),

        }
        labels = {
            "destination":"Destination:",
            "summary":"Summary:",
            "start_date":"Started on:",
            "duration":"Duration:",
            "image_url":"Image URL:",

        }

class TripEditForm(TripBaseForm):
    class Meta(TripBaseForm.Meta):
        labels = {
            "destination": "Destination:",
            "summary": "Summary:",
            "start_date": "Started on:",
            "duration": "Duration:",
            "image_url": "Image URL:",

        }


class TripDeleteForm(TripBaseForm):
    pass
