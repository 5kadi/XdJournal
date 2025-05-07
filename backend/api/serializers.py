from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, CharField

from .models import *


class MediaSerializer(ModelSerializer):
    class Meta:
        model = Media
        fields = '__all__'
        extra_kwargs = {
            'author': {
                'write_only': True
            }, #No need to get info about an author yet
        }

class ArticleSerializer(ModelSerializer):
    related_media = MediaSerializer(required=False, many=True)
    class Meta:
        model = Article
        fields = '__all__'

class UserSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            'id',
            'username',
            'password'
        ]
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }
        
    #password somehow won't be hashed without this function
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user 