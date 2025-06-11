from django.db import models

from traveler.validators import TravelerNicknameValidator


# Create your models here.
class Traveler(models.Model):
    nickname = models.CharField(max_length=30, unique=True,
            validators=[TravelerNicknameValidator()], help_text="*Nicknames can contain only letters and digits.")
    email = models.EmailField(unique=True)
    country = models.CharField(max_length=3)
    about_me = models.TextField(blank=True, null=True)
