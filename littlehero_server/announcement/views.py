from django.shortcuts import render
from rest_framework import viewsets, generics
from .serializers import *
from .models import Post
import django_filters
from .filters import *
from rest_framework.pagination import PageNumberPagination

# Create your views here.

# view when you click the title of post.
# you need regist_no and site_domain in query 
class PostViewDetail(generics.ListAPIView) :
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostDetailSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_class = PostDetailFilter


# pagination
class PostPagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'page_size'

# query handling of notice board
class PostView(generics.ListAPIView) :
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_class = PostFilter
    pagination_class = PostPagination


# update likes
class LikeView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = LikeCreateSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_class = PostDetailFilter