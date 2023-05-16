from rest_framework import serializers
from .models import Anunci
from .models import Usuari

class AnunciSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anunci
        fields = ['foto', 'titol', 'name', 'data', 'description', 'preu']

class UsuariSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuari
        fields = ['user', 'name', 'adress', 'zip_code', 'email', 'phone','avatar','bio']