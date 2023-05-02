from rest_framework import serializers
from .models import Anunci

class AnunciSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anunci
        fields = ['foto', 'titol', 'name', 'data', 'description', 'preu']