from re import M
from django.db import models

# Create your models here.

class URL(models.Model):
    url_long = models.CharField(max_length=500)
    url_custom = models.CharField(max_length=20, unique=True)

    def __str__(self) -> str:
        return self.url_custom