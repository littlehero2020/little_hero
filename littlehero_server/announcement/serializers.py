from rest_framework import serializers, generics
from .models import Post, Dropdown

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

class LikeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'regist_no',
            'site_domain',
            'like',
        )


class DropDownSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dropdown
        fields = ['li']
