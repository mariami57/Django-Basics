from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models

from organizer.validators import CompanyNameValidator, SecretKeyValidator


# Create your models here.
class Organizer(models.Model):
    company_name = models.CharField(max_length=110,
            validators=[MinLengthValidator(2), CompanyNameValidator()])
    phone_number = models.CharField(max_length=15, unique=True, validators=[RegexValidator(r'^\d+$', 'Enter digits only')])
    secret_key = models.CharField(max_length=4, validators=[SecretKeyValidator()],)
    website = models.URLField(null=True, blank=True)