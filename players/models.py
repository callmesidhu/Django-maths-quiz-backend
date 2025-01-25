# models.py
from django.db import models # type: ignore

class Players(models.Model):
    name = models.CharField(max_length=100)  # Name column with max length 100

