from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(TypeClient)
admin.site.register(AdresseClient)
admin.site.register(Client)
admin.site.register(AdressePretataire)
admin.site.register(Type_Article)
admin.site.register(TypeLogistique)
admin.site.register(Article)
admin.site.register(Commande)
admin.site.register(Categorie_Article)
admin.site.register(CategoriePrestataire)
admin.site.register(Facture)
admin.site.register(Pack_Article)
admin.site.register(Prix_Pack)
admin.site.register(Prestataire_Service)
admin.site.register(Service)
admin.site.register(Tarification)
admin.site.register(Mode_Paiement)
admin.site.register(BonCommande)

