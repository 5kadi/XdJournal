from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import *

class ArticleMediaSerializer(ModelSerializer):
    class Meta:
        model = ArticleMedia
        fields = '__all__'
        extra_kwargs = {
            'author': {
                'write_only': True
            }, #No need to get info about an author yet
        }