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
            "nickname": forms.TextInput(attrs={"placeholder": "Enter a unique nickname...", }, ),
            "email": forms.EmailInput(attrs={"placeholder":"Enter a valid email address...", }, ),
            "country":forms.TextInput(attrs={"placeholder":"Enter a country code like <BGR>...", }, ),

        }

        labels={
            "nickname":"Nickname:",
            "email": "Email:",
            "country":"Country:",

        }

class TravelerEditForm(forms.ModelForm):
    class Meta(TravelerBaseForm.Meta):
        exclude = ()
        # model = Traveler
        # fields = '__all__'
        # help_texts = {
        #     "nickname": "*Nicknames can contain only letters and digits."
        # }
        # labels = {
        #     "nickname": "Nickname:",
        #     "email": "Email:",
        #     "country": "Country:",
        #     "about_me": "About me:",
        # }


class TravelerDeleteForm(TravelerBaseForm):
    ...

