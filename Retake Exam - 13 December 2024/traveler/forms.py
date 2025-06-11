from django import forms

from traveler.models import Traveler


class TravelerBaseForm(forms.ModelForm):
    class Meta:
        model = Traveler
        fields = '__all__'


class TravelerCreateForm(TravelerBaseForm):
    ...

class TravelerEditForm(TravelerBaseForm):
    ...

class TravelerDeleteForm(TravelerBaseForm):
    ...

