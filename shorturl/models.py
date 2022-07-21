import secrets
from string import ascii_uppercase, ascii_lowercase, digits
from xmlrpc.client import TRANSPORT_ERROR
from django.db import models

# Create your models here.

class URL(models.Model):
    url_long = models.CharField(max_length=500, unique=True)
    url_custom = models.CharField(max_length=20, unique=True)


    def __str__(self) -> str:
        return self.url_custom


    def create_short_url(self, length: int = 8) -> str:
        chars = ascii_uppercase + ascii_lowercase + digits
        return "".join(secrets.choice(chars) for _ in range(length))
