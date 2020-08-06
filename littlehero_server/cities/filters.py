from django_filters import rest_framework as fils
from rest_framework import generics
from .models import *

class CitiesTableFilter(fils.FilterSet) :
    city = fils.CharFilter(field_name='city')

    class Meta :
        model = CitiesTable
        fields = ['city']
