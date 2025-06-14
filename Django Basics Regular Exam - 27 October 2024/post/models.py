from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db import models

from author.models import Author


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50, validators=[MinLengthValidator(5)],unique=True)
    image_url = models.URLField()
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='posts')