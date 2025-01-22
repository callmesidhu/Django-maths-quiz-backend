# models.py
from django.db import models

class Player(models.Model):
    id = models.AutoField(primary_key=True)  # Auto-incremented ID
    name = models.CharField(max_length=100)  # Name column with max length 100

    def __str__(self):
        return self.name
