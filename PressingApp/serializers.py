from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
import datetime

# from djoser.serializers import UserCreateSerializer,UserSerializer
#####

# class UserCreateSerializer(UserCreateSerializer):
#     class Meta(UserCreateSerializer.Meta):
#         models = Users
#         fields = ('id', 'username','fist_name','last_name','email','phone','type','password')



##GESTION DU SERIALISEUR CLIENT##

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=65, min_length=8, write_only=True)
    email = serializers.EmailField(max_length=255, min_length=4),
    first_name = serializers.CharField(max_length=255, min_length=2)
    last_name = serializers.CharField(max_length=255, min_length=2)

    class Meta:
        model = User
        fields = ['id','username','first_name','last_name','email', 'password']

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



# class TypeClientSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = TypeClient
#         fields = ['nom_type','caracteristique']




class ClientSerializers(serializers.ModelSerializer):
    # user = UserSerializer(read_only= True)
    # adresse = serializers.PrimaryKeyRelatedField(many = True, read_only = True)
    class Meta:
        model = Client
        fields = ['user','prenom','telephone','type_client','adresse']
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

## PACK ARTICLE ##
class PackSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pack_Article
        fields = ('__all__')

class ArticleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Article
        fields = ('__all__')
        depth =1

## SERVICE SERIALIZER ##
class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = ['nom_service','caracteristique','article','pack_article']
        depth = 1


class PrestataireSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Prestataire_Service
        fields = ['enseigne_juridique','numero_imatriculation','telephone','adresse','service','user']
        depth = 1



## GESTION COMMANDE ##

class CommandeSerializer(serializers.ModelSerializer):
    # client = serializers.PrimaryKeyRelatedField(allow_null = True, queryset = Client.objects.all(), required = False)
    # prestataire = serializers.PrimaryKeyRelatedField(many = True, read_only = True)

    class Meta:
        model = Commande
        fields = ['client','date_commande','mode_paiement']
    


## GESTION DE LIGNE DE COMMANDE ##

class LigneCommandeSerializer(serializers.ModelSerializer):
    # commande = CommandeSerializer(read_only = True)
    # prestataire = PrestataireSerializer(read_only = True)

    class Meta:

        model = Ligne_commande
        fields = ['quantite','date_commande','commande','prestataire','tarification']
        depth = 1
    

## GESTION DES PRIX ARTICLES ##

class PrixPackSerializer(serializers.ModelSerializer):

    class Meta:
        model = Prix_Pack
        fields = ('__all__')


## Tarification Des articles##
class TarificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tarification
        fields = ('__all__')
        depth = 1
    

## GESTION DES FACTURES ##
class FactureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Facture
        fields = ['numero_Facture','date_paiement','commande']
        depht = 1
    
        def validate(self, attrs):
            email = attrs.get('email', '')
            if User.objects.filter(email=email).exists():
                raise serializers.ValidationError(
                    {'email': ('Email is already in use')})
            return super().validate(attrs)

        def create(self, validated_data):
            return User.objects.create_user(**validated_data)


    

class NoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = ('__all__')

