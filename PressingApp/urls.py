from django.urls import path,include
from . import views
from django.urls import path,include
from. import views
from .views import  *
from rest_framework.routers import DefaultRouter
from django.conf.urls import url


router = DefaultRouter()

router.register('register',AuthentificationViewSet, basename = 'register')
router.register('order', CommandeViewSet, basename = 'commande')
router.register('service', ServiceViewSet, basename = 'service')
router.register('article', ArticleViewSet, basename = 'article')
router.register('pack', PackArticleViewset , basename = 'pack')
router.register('tarif', TarificationViewSet, basename = 'tarif')
router.register('prixpack', PackArticleViewset , basename = 'adresse')
router.register('categoriearticle', CategorieArticleViewset, basename = 'categorie')
router.register('orderItem', LigneViewSet, basename = 'lignecommande')
router.register('orderItem',PrixPackViewSet , basename = 'prixpack')
router.register('facture',FacturationViewset , basename = 'facture')
router.register('prestataire', PrestataireView , basename = 'prestataire')


urlpatterns = [
    path('',views.home, name = 'home'),
    path('registers', views.register, name ='register'),
    path('logins', views.loginClient, name = 'login'),
    path('prestaire', views.prestataire, name = ''),

     #url des API
    path('viewset/', include(router.urls)),
    path('login', LoginView.as_view()),
    # path('prestataire', PrestataireView.as_view()),
    path('search',SearchView.as_view()),
    # path('search_dist',Recherche.as_view()),
    

    #use the djoser
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),

    path('adresseclient', AdresseClientView.as_view() ),
    path('registerclient', RegisterClientView.as_view()),

]









