from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')




class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ('prenom','telephone','adresse','user')
        exclud = []


class AdresseForm(ModelForm):
    class Meta:
        model = AdresseClient
        fields = ['ville','quartier','description','longitude','latitude']



class Prestataire_serviceForm(ModelForm):

    class Meta:
        model = Prestataire_Service
        fields = ['user','photo','enseigne_juridique','numero_imatriculation','telephone','adresse','service','logistique','nom_categorie']


class ServiceForm(ModelForm):
    
    class Meta:
        model = Service
        fields = ['nom_service','caracteristique','article','pack_article','avis_client']



class TarificatioForm(ModelForm):

    class Meta:
        model = Tarification
        fields = ('__all__')

class PrixPackForm(ModelForm):

    class Meta:
        model = Prix_Pack
        fields = ('__all__')

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ('__all__')


