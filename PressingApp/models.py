from django.db import models
from django.contrib.auth.models import User
# Create your models here.



# client 

class AdresseClient(models.Model):
    ville = models.CharField(max_length = 100, blank = True, null = True)
    quartier = models.CharField(max_length = 100, blank = True, null = True)
    description = models.TextField(max_length = 300, blank = True, null = True)
    longitude = models.DecimalField(max_digits=8, decimal_places=2,  null= True, blank = True)
    latitude =  models.DecimalField(max_digits=8, decimal_places=2, null= True, blank = True)
    

    def __str__(self):
        return self.ville


class TypeClient(models.Model):
    nom_type = models.CharField(max_length = 100,blank = True)
    caracteristique = models.TextField(max_length = 200, blank = True)

    def __str__(self):
        return self.nom_type


class Client(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    prenom  = models.CharField(max_length = 100, null = True, blank = True)
    telephone = models.CharField(max_length = 100, null = True, blank = True)
    #adresse_client = models.ManyToManyField(AdresseClient, null = True , blank = True)
    typeclient = models.ForeignKey(TypeClient,on_delete = models.CASCADE, blank = True, null = True)

    def __str__(self):

        return self.prenom





#Gestion Prestataire
    
class AdressePretataire(models.Model):
    ville = models.CharField(max_length = 100, null =  True, blank = True)
    quartier = models.CharField(max_length = 100, null = True , blank = True)
    Bp = models.CharField(max_length = 10, null = True , blank = True)  
    longitude = models.DecimalField(max_digits=8, decimal_places=2)
    latitude =  models.DecimalField(max_digits=8, decimal_places=2)
   
    def __str__(self):
        return self.ville



class CategoriePrestataire(models.Model):
    nom_categorie = models.CharField(max_length = 100, blank = True)
    caracteristique = models.TextField(max_length = 100, blank = True , null = True)

    def __str__(self):
        return self.nom_categorie
    

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

    pass

    

class Prestataire_Service(models.Model):
    user = models.OneToOneField(User , on_delete = models.CASCADE)
    enseigne_juridique = models.CharField(max_length = 100)
    numero_imatriculation = models.CharField(max_length =  100, null = True, blank = True)
    telephone = models.CharField(max_length = 10, null = True , blank = True)
    adresse = models.ForeignKey(AdressePretataire, on_delete = models.CASCADE)
    service = models.ForeignKey(Service, on_delete = models.CASCADE)
    logistique = models.ManyToManyField(Logistique,)
    
    def __str__(self):
        return self.enseigne_juridique


class Mode_Paiement(models.Model):
    nom_mode = models.CharField(max_length = 100)
    caracteristique = models.TextField(max_length = 200)     

    def __str__(self):
        return self.nom_mode    


class Commande(models.Model):
    date_commande = models.DateTimeField(auto_now_add = True, null = True, blank = True )
    status = models.BooleanField(default = False, blank = True )
    mode_paiement = models.ManyToManyField(Mode_Paiement, through = 'BonCommande')


class BonCommande(models.Model):
    numero_bon = models.CharField(max_length = 100, null = True, blank = True)
    commande = models.ForeignKey(Commande , on_delete = models.CASCADE)
    mode_paiement = models.ForeignKey(Mode_Paiement, on_delete = models.CASCADE)

class Facture(models.Model):
    numero_Facture = models.CharField(max_length = 12, unique = True)
    date_paiement = models.DateTimeField(auto_now_add = True, blank = True)
    bon_commande = models.ForeignKey(BonCommande, on_delete = models.CASCADE)

    def __str__(self):
        return  self.numero_Facture
