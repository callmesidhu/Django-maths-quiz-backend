# Generated by Django 5.1.5 on 2025-01-25 21:05

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("players", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="players",
            name="time",
            field=models.DecimalField(
                decimal_places=5, default=Decimal("0.00000"), max_digits=10
            ),
        ),
    ]
