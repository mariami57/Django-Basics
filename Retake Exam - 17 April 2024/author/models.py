from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db import models

from author.validators import CapNameValidator


# Create your models here.
class Profile(models.Model):
    nickname = models.CharField(max_length=20, unique=True,
            validators=[MinLengthValidator(2,message="Nickname must be at least 2 chars long!")])
    first_name = models.CharField(max_length=30, validators=[CapNameValidator()])
    last_name = models.CharField(max_length=30, validators=[CapNameValidator()])
    chef = models.BooleanField(default=False)
    bio = models.TextField(blank=True, null=True)
