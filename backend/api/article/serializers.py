from django.contrib.auth import get_user_model
from .models import Article
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from api.auth.serializers import UserSerializer
from api.media.serializers import ArticleMediaSerializer


class ArticleSerializer(ModelSerializer):
    related_media = ArticleMediaSerializer(required=False, many=True)
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