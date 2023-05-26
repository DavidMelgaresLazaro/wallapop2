from rest_framework import serializers
from .models import Anunci,Usuari,Comentari
from django.contrib.auth.models import User

class AnunciSerializer(serializers.ModelSerializer):

    name = serializers.StringRelatedField(many=False)

    class Meta:
        model = Anunci
        fields = ['url', 'id' ,'foto', 'titol', 'name', 'data', 'description', 'preu']

    def create(self, validated_data):
        # Perform additional actions before saving the data, if needed
        # For example, you can associate the data with the current user

        print(validated_data)

        # Save the data
        return super().create(validated_data)

class UsuariSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuari
        fields = ['url','user', 'name', 'adress', 'zip_code', 'email', 'phone','avatar','bio']

class ComentariSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentari
        fields = ['name','titol','data_com','description']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user