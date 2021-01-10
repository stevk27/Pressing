from django.urls import path,include
from. import views
from .views import  *
from rest_framework.routers import DefaultRouter
from django.conf.urls import url
from .views import RegisterView, LoginView,RegisterClientView

router = DefaultRouter()

router.register('register',AuthentificationViewSet, basename = 'adresse')

urlpatterns = [
    path('',views.home, name = 'home'), 
    path('registers', views.register, name ='register'),
    path('login', views.loginClient, name = 'login'),


    #url des API
    path('viewset/', include(router.urls)),
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),

    path('registerclient', RegisterClientView.as_view())
    
]