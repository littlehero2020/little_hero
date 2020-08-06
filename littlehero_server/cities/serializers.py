from rest_framework import serializers, generics
from .models import *

class CitiesTableSerializer(serializers.ModelSerializer):
    class Meta :
        model = CitiesTable
        fields = '__all__'


class CitiesSerializer(serializers.ModelSerializer):
    class Meta :
        model = Cities
        fields = '__all__'