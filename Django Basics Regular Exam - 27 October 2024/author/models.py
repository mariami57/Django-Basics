from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db import models

from author.validators import NamesValidator, PasscodeLengthValidator


# Create your models here.
class Author(models.Model):

    first_name = models.CharField(max_length=40, validators=[MinLengthValidator(4), NamesValidator()])
    last_name = models.CharField(max_length=50, validators=[MinLengthValidator(2), NamesValidator()])
    passcode = models.CharField(max_length=6, validators=[PasscodeLengthValidator()])
    pets_number = models.PositiveSmallIntegerField()
    info = models.TextField(blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)