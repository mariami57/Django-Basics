from django import forms

from profiles.models import Profile


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('username', 'email', 'age')

        labels = {
            "username": "Username:",
            "email": "Email:",
            "age": "Age:",
        }


class ProfileCreateForm(ProfileBaseForm):
    class Meta(ProfileBaseForm.Meta):
        widgets = {"username": forms.TextInput(attrs={"placeholder": "Username"}),
                   "email": forms.TextInput(attrs={"placeholder": "Email"}),
                   "age": forms.TextInput(attrs={"placeholder": "Age"}),}

class ProfileEditForm(ProfileBaseForm):
    ...


