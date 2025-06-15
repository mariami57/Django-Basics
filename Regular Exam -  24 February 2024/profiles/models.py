from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from profiles.validators import ProfileValidator


# Create your models here.
class Profile(models.Model):
    username = models.CharField(max_length=15,
    validators=[MinLengthValidator(3, message="Username must be at least 3 chars long!") , ProfileValidator()])
    email = models.EmailField()
    age = models.IntegerField(validators=[MinValueValidator(21)])
    password = models.CharField(max_length=20)
    first_name = models.CharField(max_length=25, blank=True, null=True)
    last_name = models.CharField(max_length=25, blank=True, null=True)
    profile_picture = models.URLField(blank=True, null=True)