from django.db import models
# from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
# Create your models here.
from math import cos, asin, sqrt, pi
import datetime
from .utils import create_new_ref_number


# client 

class AdresseClient(models.Model):
    ville = models.CharField(max_length = 100, blank = True, null = True)
    quartier = models.CharField(max_length = 100, blank = True, null = True)
    description = models.TextField(max_length = 300, blank = True, null = True)
    longitude = models.DecimalField(max_digits=8, decimal_places=2,  null= True, blank = True)
    latitude =  models.DecimalField(max_digits=8, decimal_places=2, null= True, blank = True)
    

    def __str__(self):
        return self.ville



class Client(models.Model):

    Choix = (
        ('entreprise','entreprise'),
        ('personne','personne'),
    )

    user = models.OneToOneField(User, on_delete = models.CASCADE, null = True)
    type_client = models.CharField(max_length = 100,blank = True, null = True, choices =  Choix)
    prenom  = models.CharField(max_length = 100, null = True, blank = True)
    telephone = models.CharField(max_length = 100, null = True, blank = True)
    adresse =  models.ManyToManyField(AdresseClient)    
    def __str__(self):

        return self.prenom





#Gestion Prestataire

class AdressePretataire(models.Model):
    ville = models.CharField(max_length = 100, null =  True, blank = True)
    quartier = models.CharField(max_length = 100, null = True , blank = True)
    Bp = models.CharField(max_length = 10, null = True , blank = True)  
    longitude_presta = models.DecimalField(max_digits=199, decimal_places=15)
    latitude_presta =  models.DecimalField(max_digits=199, decimal_places=15)
   
    def __str__(self):
        return self.ville
    
    # def distance(self,latitude_client, longitude_client, latitude_presta, longitude_presta ):
    #     p = pi/180
    #     a = 0.5 - cos((self.latitude_presta-latitude_client)*p)/2 + cos(latitude_client*p) * cos(latitude_presta*p) * (1-cos((longitude_presta-longitude_client)*p))/2
    #     return 12742 * asin(sqrt(a))
        




#Gestion des  Articles

class Type_Article(models.Model):
    nom_type =  models.CharField(max_length  = 100, blank = True)

    def __str__(self):
        return self.nom_type

class Categorie_Article(models.Model):

    Select = (
        ('Femme','Femme'),
        ('Homme', 'Homme'),
        ('Enfant','Enfant'),
        ('Bebe','Bebe'),
    )

    nom_categorie = models.CharField(max_length = 100, blank = True, choices = Select)


    def __str__(self):
        return self.nom_categorie

class Article(models.Model):
    Choix = (
        ('L','L'),
        ('M','M'),
        ('XL','XL'),
        ('XXL','XXL'),
        ('XXXL', 'XXXL'),
        ('autres','autres')
    )

    couleur = models.CharField(max_length = 100, null = True , blank = True)
    taille = models.CharField(max_length = 100, null = True , blank = True, choices = Choix)
    marque = models.CharField(max_length = 100, blank = True)
    description = models.TextField(max_length = 300, null = True , blank = True)
    categorie_article = models.ForeignKey(Categorie_Article, on_delete = models.CASCADE, blank = True)
    type_article = models.ForeignKey(Type_Article, on_delete = models.CASCADE, null = True, blank = True)


class Pack_Article(models.Model):
    poids = models.PositiveIntegerField()
    autre_detailles = models.TextField(max_length = 300, null = True, blank = True)



class Service(models.Model):
    Types = (
        ('classique','classique'),
        ('express', 'express'),
        ('autres','autre'),
    ) 


    nom_service = models.CharField(max_length = 100, blank = True, choices = Types)
    caracteristique = models.TextField(max_length = 300, blank = True)
    article = models.ManyToManyField(Article, through = 'Tarification')
    pack_article = models.ManyToManyField(Pack_Article, through = 'Prix_Pack')
    avis_client =models.ManyToManyField(Client, through = 'Note')

    def __str__(self):
        return self.nom_service
        


class Note(models.Model):
    service = models.ForeignKey(Service, on_delete = models.CASCADE, blank = True)
    client =  models.ForeignKey(Client, on_delete = models.CASCADE, null = True, blank = True)
    commentaire =  models.TextField(max_length = 300, null = True, blank = True)



class Tarification(models.Model):
    article = models.ForeignKey(Article, on_delete = models.CASCADE, null = True, blank = True)
    prix = models.PositiveIntegerField()
    service = models.ForeignKey(Service, on_delete = models.CASCADE, null = True, blank = True)



class Prix_Pack(models.Model):
    prix = models.PositiveIntegerField()
    service = models.ForeignKey(Service, on_delete = models.CASCADE, null = True, blank = True)
    pack_article = models.ForeignKey(Pack_Article, on_delete = models.CASCADE, null = True, blank = True)


class TypeLogistique(models.Model):
    nom_type = models.CharField(max_length = 100)
    caracteristique = models.TextField(max_length = 200)

    def __str__(self):
        return self.nom_type


class Logistique(models.Model):

    ChoixLogistique = (
        ('Ramassege','Ramassage'),
        ('Livraison','Livraison'),
    )
    service = models.CharField(max_length = 100, choices = ChoixLogistique, null = True)
    nom = models.CharField(max_length = 100,null = True)
    prenom = models.CharField(max_length = 100,null = True)
    adresse = models.CharField(max_length = 100,null = True)
    ville = models.CharField(max_length = 100,null = True)
    quartier = models.CharField(max_length = 100,null = True)

    def __str__(self):
        return self.ville
    

class Prestataire_Service(models.Model):

    Prestataire = (
        ('blanchisseur','blanchisseur'),
        ('pressing','pressing'),
    )

    user = models.OneToOneField(User , on_delete = models.CASCADE, null=True)
    photo = models.ImageField()
    enseigne_juridique = models.CharField(max_length = 100, null = True, blank = True)
    numero_imatriculation = models.CharField(max_length = 100, null = True, blank = True)
    telephone = models.CharField(max_length = 10, null = True , blank = True)
    adresse = models.ForeignKey(AdressePretataire, on_delete = models.CASCADE)
    service = models.ManyToManyField(Service)
    logistique = models.ManyToManyField(Logistique,)
    nom_categorie = models.CharField(max_length = 100, blank = True, choices = Prestataire)

    def __str__(self):
        return str(self.enseigne_juridique)
    

class Commande(models.Model):

    Mode = (
        ('cash', 'cash'),
        ('electronique','electronique'),
    )

    client = models.ForeignKey(Client, on_delete = models.CASCADE, null = True, blank = True)
    date_commande = models.DateTimeField(auto_now_add = True, null = True, blank = True )
    # status = models.BooleanField(default = False, blank = True )

    mode_paiement = models.CharField(max_length = 100, null = True, blank = True, choices = Mode)
    adresse_livraison =  models.ForeignKey(AdresseClient, on_delete = models.CASCADE, related_name = 'livraison' , null = True)
    adresse_ramassage = models.ForeignKey(AdresseClient, on_delete = models.CASCADE , related_name = 'ramassage' ,null = True, blank = True)
    tarification = models.ManyToManyField(Tarification, through = 'Ligne_commande')

    #montant total
    @property
    def total_price(self):
        orderItem = self.tarification_set.all()
        total = sum(article.prix_article for article in orderItem)
        return total 

    #quantite total
    @property
    def quantite_total(self):
        orderItem = self.tarification_set.all()
        total = sum(article.quantite for article in orderItem)
        return total



class Ligne_commande(models.Model):
    quantite = models.PositiveIntegerField()
    date_commande = models.DateTimeField(auto_now_add = True, blank = True, null = True)
    commande = models.ForeignKey(Commande, on_delete = models.CASCADE, null = True, blank = True)
    prestataire = models.ForeignKey(Prestataire_Service, on_delete = models.CASCADE , null = True , blank = True)
    tarification = models.ForeignKey(Tarification, on_delete = models.CASCADE, null = True , blank = True)

    @property
    def prix_article(self):
        price = self.quantite*self.tarification.prix
        return price


        pass




class Facture(models.Model):
    commande = models.ForeignKey(Commande, on_delete = models.CASCADE, null = True, blank = True)
    numero_Facture = models.CharField(max_length = 12, unique = True)
    date_paiement = models.DateTimeField(auto_now_add = True, blank = True)
        



    
