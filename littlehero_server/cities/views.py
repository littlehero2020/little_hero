from django.shortcuts import render
from rest_framework import viewsets, generics
from .serializers import *
from .models import *
import django_filters
from .filters import *

# Create your views here.

# view when you click the title of post.
# you need regist_no and site_domain in query 
class CitiesTableView(generics.ListAPIView) :
    queryset = CitiesTable.objects.all()
    serializer_class = CitiesTableSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_class = CitiesTableFilter

class CitiesView(generics.ListAPIView):
    queryset = Cities.objects.all()
    serializer_class = CitiesSerializer