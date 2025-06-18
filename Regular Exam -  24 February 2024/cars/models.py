from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from cars.validators import YearValidator



# Create your models here.
class Car(models.Model):

    class TypeCarChoices(models.TextChoices):
        RALLY = "Rally", "Rally"
        OPEN_WHEEl = "Open-wheel", "Open-wheel"
        KART = "Kart", "Kart"
        DRAG = "Drag", "Drag"
        OTHER = "Other", "Other"

    type = models.CharField(choices=TypeCarChoices.choices, max_length=10)
    model = models.CharField(max_length=15, validators=[MinLengthValidator(1)])
    year = models.IntegerField(validators=[YearValidator()])
    image_url = models.URLField(unique=True)
    price = models.FloatField(validators=[MinValueValidator(1.0)])
    owner = models.ForeignKey('profiles.Profile', on_delete=models.CASCADE, related_name='cars')