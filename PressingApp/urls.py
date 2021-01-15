from django.urls import path,include
from. import views
from .views import  *
from rest_framework.routers import DefaultRouter
from django.conf.urls import url


router = DefaultRouter()

router.register('register',AuthentificationViewSet, basename = 'adresse')
# router.register('commande',LigneViewSet, basename = 'search')
router.register('order', CommandeViewSet, basename = 'commande')
router.register('service', ServiceViewSet, basename = 'service')
router.register('article', ArticleViewSet, basename = 'article')


urlpatterns = [
    path('',views.home, name = 'home'), 
    path('registers', views.register, name ='register'),
    path('logins', views.loginClient, name = 'login'),
    

    #url des API
    path('viewset/', include(router.urls)),
    # path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    # path('recherche', PrestataireView.as_view()),
    # path('search',SearchView.as_view()),
    # path('lignecommande',LigneCommandeView.as_view()),
  


    #use the djoser
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),

    path('adresseclient', AdresseClientView.as_view() ),
    # path('typeclient', TypeClientView.as_view() ),
    path('registerclient', RegisterClientView.as_view())
    
]