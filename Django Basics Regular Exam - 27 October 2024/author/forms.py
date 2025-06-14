from django import forms

from author.models import Author


class AuthorBaseForm(forms.ModelForm):
    class Meta:
        model = Author
        exclude = ('info', 'image_url')

        help_texts = {
            "passcode": "Your passcode must be a combination of 6 digits"
        }
        error_messages = {
            "passcode": {
                "max_length":"Your passcode must be exactly 6 digits!"
            }
        }

class AuthorCreateForm(AuthorBaseForm):
    class Meta(AuthorBaseForm.Meta):
        widgets = {
            "first_name": forms.TextInput(attrs={"placeholder": "Enter your first name..."}),
            "last_name": forms.TextInput(attrs={"placeholder": "Enter your last name..."}),
            "passcode": forms.PasswordInput(attrs={"placeholder": "Enter 6 digits..."}),
            "pets_number": forms.TextInput(attrs={"placeholder": "Enter the number of your pets..."}),
        }

        labels = {
            "first_name": "First Name:",
            "last_name": "Last Name:",
            "passcode": "Passcode:",
            "pets_number": "Pets Number:",
        }

class AuthorEditForm(AuthorBaseForm):
    class Meta(AuthorBaseForm.Meta):
        exclude = ("passcode",)

        labels = {"info": "Info:",
                  "image_url": "Profile Image URL:",}


class AuthorDeleteForm(AuthorBaseForm):
    ...