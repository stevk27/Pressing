from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

##GESTION DU SERIALISEUR CLIENT##

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=65, min_length=8, write_only=True)

    email = serializers.EmailField(max_length=255, min_length=4),
    first_name = serializers.CharField(max_length=255, min_length=2)
    # last_name = serializers.CharField(max_length=255, min_length=2)

    class Meta:
        model = User
        fields = ['id','username','first_name','email', 'password']

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


class AdresseSerializer(serializers.ModelSerializer):

    class Meta:
        model = AdresseClient
        fields = ['id','ville', 'quartier','description','longitude','latitude',]



class TypeClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = TypeClient
        fields = ['id','nom_type','caracteristique']




class ClientSerializers(serializers.ModelSerializer):
   
    class Meta:
        model = Client
        fields = ['id','user','prenom','telephone','typeclient']
        depth = 1


## PRESTATAIRE SERIALIZER ##
class AdressePrestatireSerializer(serializers.ModelSerializer):

    class Meta:
        model = AdressePretataire
        fields = ['id','ville','quartier','Bp']


## SERIALIZER ARTICLE PRESTATAIRE ##
class TypeArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Type_Article
        fields = ['id','nom_type']

class CategorieArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categorie_Article
        fields = ['id','nom_categorie']


class ArticleSerializer(serializers.ModelSerializer):
    
    type_article = TypeArticleSerializer(many = False)
    categorie_article = CategorieArticleSerializer(many = False)

    class Meta:
        model = Article
        fields = ['couleur','taille','marque','description','cartegorieArticle','type_article']


## SERVICE SERIALIZER ##
class ServiceSerializer(serializers.ModelSerializer):



    class Meta:
        model = Service
        fields = ['nom_service','caracteristique','article','pack_article']


class PrestataireSerializer(serializers.ModelSerializer):


    class Meta:
        model = Prestataire_Service
        fields = ['enseigne_juridique','numero_imatriculation','telephone','adresse','service','user']



## GESTION COMMANDE ##

class CommandeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Commande
        fiedls = []