from django.db import models  # type: ignore
from decimal import Decimal

class Players(models.Model):
    name = models.CharField(max_length=100)  # Name column with max length 100
    time = models.DecimalField(max_digits=10, decimal_places=5, default=Decimal('0.00000'))  # Time column with default value 0.00000
    point = models.IntegerField(default=0)  # Score column with default value 0

    def __str__(self):
        return self.name
