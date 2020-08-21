import json
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, generics
from rest_framework.filters import SearchFilter
from .serializers import *
from .models import Post
import django_filters
from .filters import *
from rest_framework.pagination import PageNumberPagination
from django.views.decorators.http import require_POST
from django.http import HttpResponse

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
    filter_backends = (SearchFilter, django_filters.rest_framework.DjangoFilterBackend,)
    filter_class = PostFilter
    pagination_class = PostPagination
    search_fields = ['title']


# update likes
class LikeView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = LikeCreateSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_class = PostDetailFilter
        
def post_like(request) :
    registNo = request.POST.get('regist_no', None)
    siteDomain = request.POST.get('site_domain', None)
    post = get_object_or_404(Post, regist_no=registNo, site_domain=siteDomain)
    user = request.user
        
    if post.likes_post.filter(id=user.id).exists() :
        post.likes_post.remove(user)
        post.like_count -= 1
        message = '좋아요 취소'
    else :
        post.likes_post.add(user)
        post.like_count += 1
        message = '좋아요'

    referer_url = request.META.get('HTTP_REFERER')
    path = urlparse(referer_rul).path
    return HttpResponseRedirect(path)
    
# get dropdown
class DropDownView(generics.ListAPIView):
    queryset = Dropdown.objects.all()
    serializer_class = DropDownSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_class = DropDownFilter
