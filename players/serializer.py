# serializers.py
from rest_framework import serializers # type: ignore
from .models import Players

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Players
        fields = '__all__'
