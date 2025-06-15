from django import forms

from cars.mixins import ReadOnlyMixin
from cars.models import Car


class CarBaseForm(forms.ModelForm):
    class Meta:
        model = Car
        exclude = ("owner",)

        error_messages = {
            "image_url":{
                "unique":"This image URL is already in use! Provide a new one."
            }
        }

        labels ={
            "type": "Type:",
            "model": "Model:",
            "year": "Year:",
            "image_url": "Image URL:",
            "price": "Price:",
        }

class CarCreateForm(CarBaseForm):
    class Meta(CarBaseForm.Meta):
        widgets = {
            "image_url": forms.TextInput(attrs={"placeholder":"https://..."}),
        }

class CarEditForm(CarBaseForm):
    ...

class CarDeleteForm(ReadOnlyMixin, CarBaseForm):
    ...