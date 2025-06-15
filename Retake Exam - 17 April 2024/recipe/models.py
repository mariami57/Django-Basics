from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from author.models import Profile


# Create your models here.
class Recipe(models.Model):

    class Cuisines(models.TextChoices):
        FRENCH = "French","French"
        CHINESE = "Chinese", "Chinese"
        ITALIAN = "Italian", "Italian"
        BALKAN = "Balkan", "Balkan"
        OTHER  = "Other", "Other"


    title = models.CharField(max_length=100,
            validators=[MinLengthValidator(10)], unique=True)
    cuisine_type = models.CharField(choices=Cuisines, max_length=7)
    ingredients = models.TextField()
    instructions = models.TextField()
    cooking_time = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    image_url = models.URLField(blank=True, null=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)