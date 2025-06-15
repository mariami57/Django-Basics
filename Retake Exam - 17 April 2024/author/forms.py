from django import forms

from author.models import Profile


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

        labels = {
            "nickname" : "Nickname:",
            "first_name" : "First Name:",
            "last_name" : "Last Name:",
            "chef" : "Chef:",
        }

class ProfileCreateForm(ProfileBaseForm):
    class Meta(ProfileBaseForm.Meta):
        exclude = ('bio',)

class ProfileEditForm(ProfileBaseForm):
    ...

class ProfileDeleteForm(ProfileBaseForm):
    ...

