import django_filters
from django_filters import CharFilter
from .models import *


# class PrestataireFilter(django_filters.FilterSet):
#     # nom_universite = CharFilter(field_name = "nom",lookup_expr = "icontains" )
    
#     class Meta:
#         model = Prestataire()
#         fields = ['enseigne_juridique','adresse','service']
#         # exclude = ['adresse','cp','effectifs']
