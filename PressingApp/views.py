from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login , authenticate, logout
from .forms import *
from django.db.models import Q
from django.contrib.auth.hashers import make_password
# Gestion des API


from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .serializers import *
from django.views.decorators.csrf import csrf_exempt


#bibliotheques rest_framework à importer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins

#gestion des authentications avec les API
from rest_framework.authentication import SessionAuthentication, TokenAuthentication ,BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.conf import settings
from django.contrib import auth
import jwt

from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.generics import GenericAPIView

# Create your views here.

def home(request):

    return render(request,'home.html')

# INTERFACE CLIENT #


def register(request):
    if request.method == "POST" :
        forms = CreateUserForm(request.POST)
        customers = ClientForm(request.POST)
        type_client  =  TypeClientForm(request.POST)


        if forms.is_valid() and customers.is_valid() and type_client.is_valid():

            print('welcome')
            user = forms.save()
            types = type_client.save()
            client = customers.save(commit = False)
            types = type_client.save()


            client.user = user
            client.type = types
    
            print(client.user)

            client.save()
            return redirect ('login')
        else:
            print('no error')

            return  render(request, 'register.html')
    else:
        forms = CreateUserForm()
        customers = ClientForm()
        type_client  =  TypeClientForm()
        
    context = {
            'forms':forms,
            'customers': customers,
            'types':type_client,
            }
    return render(request, 'register.html', context)

def loginClient(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # la methode authenticate va verifier les information reçues username et password
        user = authenticate(request, username = username, password = password)
        print(user)
        if user is not None :
            login(request, user)
            return redirect('dasbordfournisseur')
        else :
            messages.info(request, 'username or password is incorrect')
            return  render(request, 'commerce/login.html')


    return render(request, 'login.html')




# Gestion de la recherche

def search(request):
    if request.method == "GET":
        query = request.GET.get('q')#on recupere la valeur de q

        

        if query is not None:
            lookup = Q(adresse__ville__icontains = query)|Q(adresse__quartier__icontains = query)|Q(service__nom_service__icontains = query)|Q(enseigne_juridique__icontains = query)
            result = Prestataire_Service.objects.filter(lookup).distinct() 
            context ={
                'results':result,
                }
            return render(request, 'prestataire/search.html', context )
        else:
            return render(request,'prestataire/search.html')
    else:
        return render(request,'prestataire/home.html')


## GESTION DES COMMANDES CLIENTS ##

def cart(request):
    pass

def checklist(request):
    pass

def procesOrder(request):
    pass

## GESTIONS DESARTICLES  ##
def tarifArticle(request):
    pass

def tarifPachArticle(request):
    pass



# GESTION DES API MOBIL

class AuthentificationViewSet(viewsets.ViewSet):
    serializer_class = ClientSerializers

    def get_queryset(self):
        client = Client.objects.all()
        return client

    def create(self, request, *args, **kwargs):
        data_user = request.data

        newuser = User.objects.create(
            username = data_user ["username"],
            first_name = data_user["first_name"],
            email = data_user["email"],
            password = make_password(data_user["password"]),
           
        )
        newuser.save()
        newclient = Client.objects.create(
            user = newuser,
            prenom = data_user["prenom"], 
            telephone = data_user["telephone"],
            typeclient = TypeClient.objects.get(id = data_user["typeclient"])
         )
        newclient.save()

        serializer = ClientSerializers(newclient)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
       

    
    def list(self,request):
        clients = Client.objects.all()
        serializer = ClientSerializers(clients, many = True)
        return Response(serializer.data)


#GENERIC VIEW API 

# class RegisterView(GenericAPIView):
#     serializer_class = UserSerializer
#     query = Client.objects.all()

#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        data = request.data
        username = data.get('username',)
        password = data.get('password', '')
        user = auth.authenticate(username=username, password=password)
        print(username)
        print(password)
        if user is not None:
            print("hello")
            auth_token = jwt.encode(
                {'username': user.username}, settings.SECRET_KEY)

            serializer = UserSerializer(user)

            data = {'user': serializer.data, 'token': auth_token}

            return Response(data, status=status.HTTP_200_OK)

            # SEND RES
        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)



#REGISTER CLIENT avec tous ses informations

class RegisterClientView(GenericAPIView):
    serializer_class = ClientSerializers
    

    def post(self, request):
        serializer = ClientSerializers(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AdresseClientView(GenericAPIView):
    serializer_class = AdresseSerializer
    query = AdresseClient.objects.all()

    def post(self, request):
        serializer = AdresseSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TypeClientView(GenericAPIView):

    serializer_class = TypeClientSerializer

    query = TypeClient.objects.all()

    def post(self,request):
        serializer = TypeClientSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


## API DE LA RECHERCHE ##

class SearchView(GenericAPIView):
    pass

