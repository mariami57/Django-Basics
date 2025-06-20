from django.core.validators import MinValueValidator
from django.db import models

from albums.choices import GenreChoices


# Create your models here.
class Album(models.Model):
    album_name = models.CharField(max_length=30, unique=True)
    artist = models.CharField(max_length=30)
    genre = models.CharField(choices=GenreChoices.choices, max_length=30)
    description = models.TextField(blank=True, null=True)
    image_url = models.URLField()
    price = models.FloatField(validators=[MinValueValidator(0.0)])
    owner = models.ForeignKey('profiles.Profile', related_name='owner', on_delete=models.CASCADE)