from django import forms

from event.mixins import ReadOnlyMixin
from event.models import Event


class EventBaseForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ('organizer',)

        labels = {
            'slogan': 'Slogan:',
            'location': 'Location:',
            'start_time': 'Event Date/Time:',
            'available_tickets': 'Available Tickets:',
            'key_features': 'Event Key Features:',
            'banner_url': 'Event Banner URL:',
        }

        widgets = {
            'slogan': forms.TextInput(attrs={'placeholder': 'Provide an appealing text...'}),
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'key_features': forms.Textarea(attrs={'placeholder': 'Provide important event details...'}),
            'banner_url': forms.URLInput(attrs={'placeholder': 'An optional banner image URL...'}),
        }

class EventCreateForm(EventBaseForm):
    ...

class EventEditForm(EventBaseForm):
    ...

class EventDeleteForm(ReadOnlyMixin, EventBaseForm):
    ...
