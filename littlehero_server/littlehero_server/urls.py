"""littlehero_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from announcement.models import Dropdown
from announcement.views import *
from cities.views import *
from cities.models import Cities, CitiesTable
from django.conf.urls import url, include
from rest_framework_swagger.views import get_swagger_view

from django.urls import re_path
from . import views

router = routers.DefaultRouter()
admin.site.register(Dropdown)
admin.site.register(Cities)
admin.site.register(CitiesTable)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/doc', get_swagger_view(title='Rest API Document')),
    url(r'^api/posts/dropdown', DropDownView.as_view()),
    url(r'^api/posts/all', PostView.as_view()),
    url(r'^api/posts/detail', PostViewDetail.as_view()),
    url(r'^api/posts/likes', LikeView.as_view()),
    url(r'^api/cities/list', CitiesView.as_view()),
    url(r'^api/cities/detail', CitiesTableView.as_view()),
    re_path(r'^$', views.index, name='index'),
]