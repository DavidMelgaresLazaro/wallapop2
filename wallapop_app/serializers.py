from rest_framework import serializers
from .models import Anunci
from .models import Usuari

class AnunciSerializer(serializers.ModelSerializer):

    name = serializers.StringRelatedField(many=False)

    class Meta:
        model = Anunci
        fields = ['url', 'id' ,'foto', 'titol', 'name', 'data', 'description', 'preu']

class UsuariSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuari
        fields = ['url','user', 'name', 'adress', 'zip_code', 'email', 'phone','avatar','bio']