from django.contrib import admin # type: ignore

# Register your models here.
from .models import Players

admin.site.register(Players)