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
        fields = ('prenom','telephone')
        exclud = ['adresse','typeclient','user']


class AdresseForm(ModelForm):
    class Meta:
        model = AdresseClient
        fields = ['ville','quartier','description','longitude','latitude']


class TypeClientForm(ModelForm):

    class Meta:
        model = TypeClient
        fields = ['nom_type','caracteristique']
