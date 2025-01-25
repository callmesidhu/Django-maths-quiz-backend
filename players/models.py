# models.py
from django.db import models # type: ignore

class Players(models.Model):
    name = models.CharField(max_length=100)  # Name column with max length 100
    time = models.IntegerField(default=0)  # Time column with default value 0
    point = models.IntegerField(default=0)  # Score column with default value 0
    
