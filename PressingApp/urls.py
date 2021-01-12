from django.urls import path,include
from. import views
from .views import  *
from rest_framework.routers import DefaultRouter
from django.conf.urls import url
from .views import *

router = DefaultRouter()

router.register('register',AuthentificationViewSet, basename = 'adresse')

urlpatterns = [
    path('',views.home, name = 'home'), 
    path('registers', views.register, name ='register'),
    path('logins', views.loginClient, name = 'login'),


    #url des API
    path('viewset/', include(router.urls)),
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),

    path('adresseclient', AdresseClientView.as_view() ),
    path('typeclient', TypeClientView.as_view() ),
    path('registerclient', RegisterClientView.as_view())
    
]