from django.core.validators import MinLengthValidator
from django.db import models

from traveler.validators import TravelerNicknameValidator


# Create your models here.
class Traveler(models.Model):
    COUNTRY_LENGTH = 3
    nickname = models.CharField(max_length=30, unique=True,
            validators=[TravelerNicknameValidator()], )
    email = models.EmailField(unique=True)
    country = models.CharField(max_length=COUNTRY_LENGTH, validators=[MinLengthValidator(COUNTRY_LENGTH)])
    about_me = models.TextField(blank=True, null=True)
