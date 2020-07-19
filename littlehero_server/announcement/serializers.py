from rest_framework import serializers, generics
from .models import Post

class PostDetailSerializer(serializers.ModelSerializer):
    class Meta :
        model = Post
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    class Meta :
        model = Post
        fields = (
            'regist_no',
            'title',
            'site_domain',
            'address_city',
            'address_gu',
            'recruit_status',
            'adult_status',
            'start_date',
            'end_date',
            'domain',
        )