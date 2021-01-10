from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login , authenticate, logout
from .forms import *
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




# GESTION DES API MOBIL

class AuthentificationViewSet(viewsets.ViewSet):

    def create(self,request):
        user = UserSerializer(data = request.data)
        client = ClientSerializers(data = request.data)
        type_client = TypeClientSerializer(data = request.data)

        data = {}

        if user.is_valid() and client.is_valid() and type_client.is_valid():
            user.save()
            type_client.save()
            client = client.save(commit = False) 
            client.user = user
            client.typeclient = type_client
            client.save()
            return Response(client.data, status = status.HTTP_201_CREATED)
        client = ClientSerializers()
        print(client.errors)
        return Response('errors', status = status.BAD_REQUEST)

    def list(self,request):
        clients = Client.objects.all()
        serializer = ClientSerializers(clients, many = True)
        return Response(serializer.data)


#GENERIC VIEW API 

class RegisterView(GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        data = request.data
        username = data.get('username', '')
        password = data.get('password', '')
        user = auth.authenticate(username=username, password=password)

        if user:
            auth_token = jwt.encode(
                {'username': user.username}, settings.JWT_SECRET_KEY)

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
        pass



