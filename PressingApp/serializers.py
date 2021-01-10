from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class AdresseSerializer(serializers.ModelSerializer):

    class Meta:
        model = AdresseClient
        fields = ['ville', 'quartier','description','longitude','latitude','instant']


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=65, min_length=8, write_only=True)

    email = serializers.EmailField(max_length=255, min_length=4),
    first_name = serializers.CharField(max_length=255, min_length=2)
    last_name = serializers.CharField(max_length=255, min_length=2)

    class Meta:
        model = User
        fields = ['username','email', 'password']

    def validate(self, attrs):
        email = attrs.get('email', '')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {'email': ('Email is already in use')})
        return super().validate(attrs)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=65, min_length=8, write_only=True)
    username = serializers.CharField(max_length=255, min_length=2)

    class Meta:
        model = User
        fields = ['username', 'password']




class TypeClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = TypeClient
        fields = ['nom_type','caracteristique']


class ClientSerializers(serializers.ModelSerializer):
    # adresse = serializer.PrimaryKeysRelateField()
    user =  UserSerializer(many = True)
    typesclient = TypeClientSerializer( many = False)

    class Meta:
        model = Client
        fields = ['prenom','telephone','typesclient','user']
        
    # def validate(self, attrs):
    #     email = attrs.get('email', '')
    #     if User.objects.filter(email=email).exists():
    #         raise serializers.ValidationError(
    #             {'email': ('Email is already in use')})
    #     return super().validate(attrs)

    def create(self, validated_data):
        return Client.objects.create_client(**validated_data)
