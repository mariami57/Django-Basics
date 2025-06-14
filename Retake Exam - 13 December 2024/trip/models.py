from django.core.validators import MinLengthValidator
from django.db import models
from traveler.models import Traveler


# Create your models here.
class Trip(models.Model):
    destination = models.CharField(max_length=100,validators=[MinLengthValidator(3)])
    summary = models.TextField()
    start_date = models.DateTimeField()
    duration = models.PositiveSmallIntegerField(default=1, help_text="*Duration in days is expected.")
    image_url = models.URLField(blank=True, null=True)
    traveler = models.ForeignKey(Traveler, on_delete=models.CASCADE, related_name='trips')

    class Meta:
        ordering = ['-start_date']