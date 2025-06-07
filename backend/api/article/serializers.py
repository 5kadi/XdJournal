from django.contrib.auth import get_user_model
from .models import Article, ARTICLE_CONTENT_SCHEMA
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from api.auth.serializers import UserSerializer
from api.media.serializers import ArticleMediaSerializer


class ArticleSerializer(ModelSerializer):
    #related_media = ArticleMediaSerializer(required=False, many=True)

    class Meta:
        model = Article
        fields = '__all__'


class ArticleListSerializer(ModelSerializer):
    header_media = SerializerMethodField('get_header_media')
    header_content = SerializerMethodField('get_header_text')
    user = UserSerializer(read_only=True)

    class Meta:
        model = Article
        fields = [
            'id',
            'user',
            'create_date',
            'header',
            'header_media',
            'header_content'
        ]

    def get_header_media(self, obj: Article):
        #print(obj.content)
        media_block = None
        for block in obj.content:
            print(block)
            if block["type"] == "media":
                media_block = block
                break
        
        if not media_block:
            return ""
        else:
            return media_block["content"]

    def get_header_text(self, obj: Article) -> str: 
        for block in obj.content:
            if block["type"] == "text":
                return block["content"][:250] + " ..."