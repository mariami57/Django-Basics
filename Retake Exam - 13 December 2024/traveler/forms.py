from django import forms

from traveler.models import Traveler


class TravelerBaseForm(forms.ModelForm):
    class Meta:
        model = Traveler
        exclude = ('about_me', )

        help_texts = {
            "nickname": "*Nicknames can contain only letters and digits."
        }


class TravelerCreateForm(TravelerBaseForm):
    class Meta(TravelerBaseForm.Meta):
        widgets = {
            "nickname": forms.TextInput(attrs={"placeholder": "Enter a unique nickname...", "label": "Nickname:"}, ),
            "email": forms.EmailInput(attrs={"placeholder":"Enter a valid email address...", "label": "Email:"}, ),
            "country":forms.TextInput(attrs={"placeholder":"Enter a country code like <BGR>...", "label": "Country:"}, ),

        }

class TravelerEditForm(TravelerBaseForm):
    ...

class TravelerDeleteForm(TravelerBaseForm):
    ...

