from django import forms

from profiles.models import Profile


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

        help_texts = {
            "age": "Age requirement: 21 years and above."
        }

        widgets = {
            "password": forms.PasswordInput(),
        }

        labels = {
            "username": "Username:",
            "email": "Email:",
            "age":"Age:",
            "password": "Password:",
            "first_name": "First Name:",
            "last_name": "Last Name:",
            "profile_picture": "Profile Picture:",

        }

class ProfileCreateForm(ProfileBaseForm):
    class Meta(ProfileBaseForm.Meta):
        fields = ('username', 'email', 'age', 'password')

class ProfileEditForm(ProfileBaseForm):
    ...


class ProfileDeleteForm(ProfileBaseForm):
    ...