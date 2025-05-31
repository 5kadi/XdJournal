from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.utils.encoding import force_str
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import *





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
    

class ArticleMediaSerializer(ModelSerializer):
    class Meta:
        model = ArticleMedia
        fields = '__all__'
        extra_kwargs = {
            'author': {
                'write_only': True
            }, #No need to get info about an author yet
        }

class ArticleSerializer(ModelSerializer):
    related_media = ArticleMediaSerializer(required=False, many=True)
    class Meta:
        model = Article
        fields = '__all__'

class ArticleListSerializer(ModelSerializer):
    header_media = SerializerMethodField('get_header_media')
    header_content = SerializerMethodField('get_header_text')
    author = UserSerializer(read_only=True)
    class Meta:
        model = Article
        fields = [
            'id',
            'author',
            'create_date',
            'header',
            'header_media',
            'header_content'
        ]

    def get_header_media(self, obj: Article):
        media_frag = None
        for frag in obj.content.values():
            if frag["type"] == "media":
                media_frag = frag
                break
        
        if not media_frag:
            return ""
        else:
            return media_frag["content"]

    def get_header_text(self, obj: Article) -> str:
        header_frag  = next(iter(obj.content.values())) #first item is always a text
        return header_frag["content"][:250] + " ..."