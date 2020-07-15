from django_filters import rest_framework as fils
from rest_framework import generics
from .models import Post

class PostDetailFilter(fils.FilterSet) :
    registNo = fils.NumberFilter(field_name='regist_no')
    siteDomain = fils.NumberFilter(field_name='site_domain')

    class Meta :
        model = Post
        fields = ['registNo', 'siteDomain']


class PostFilter(fils.FilterSet) :
    addressCity = fils.CharFilter(field_name='address_city')
    addressGu = fils.CharFilter(field_name='address_gu')
    recruitStatus = fils.BooleanFilter(field_name='recruit_status')
    adultStatus = fils.BooleanFilter(field_name='adult_status')

    startDate = fils.DateFilter(field_name='start_date', lookup_expr=('gte')) #greater or equal
    endDate = fils.DateFilter(field_name='end_date', lookup_expr=('lte')) #less of equal
    
    
    class Meta :
        model = Post
        fields = [
            'addressCity',
            'addressGu',
            'recruitStatus',
            'adultStatus',
            'startDate',
            'endDate',
        ]
    