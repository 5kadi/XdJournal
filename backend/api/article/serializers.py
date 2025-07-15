from django.contrib.auth import get_user_model
from .models import Article, ARTICLE_CONTENT_SCHEMA
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from api.serializers import ReadOnlyModelSerializer, CustomKwargsMixin
from api.auth.serializers import UserListSerializer
from api.media.serializers import ArticleMediaSerializer

#for creating articles
class ArticleCreateSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

#for individual article data   
class ArticleGetSerializer(ReadOnlyModelSerializer):
    like_count = SerializerMethodField('get_like_count')
    comment_count = SerializerMethodField('get_comment_count')
    user = UserListSerializer()

    class Meta:
        model = Article
        fields = "__all__"

    def get_like_count(self, obj: Article) -> int:
        return obj.api_articlelike.count()
    
    def get_comment_count(self, obj: Article) -> int:
        return obj.api_comment.count()
    
#URD = user related data Xd
class ArticleURDGetSerializer(ArticleGetSerializer, CustomKwargsMixin):
    is_owner = SerializerMethodField('get_is_owner')
    is_liked = SerializerMethodField('get_is_liked')
    
    class Meta:
        model = Article
        fields = "__all__"
    
    def get_is_owner(self, obj: Article) -> bool:
        request_user = self.custom_kwargs["request_user"]
        return request_user == obj.user
    
    def get_is_liked(self, obj: Article) -> bool:
        request_user = self.custom_kwargs["request_user"]
        return bool(obj.api_articlelike.filter(user=request_user.id).count())

#for multiple articles on main page
class ArticleListSerializer(ReadOnlyModelSerializer):
    header_media = SerializerMethodField('get_header_media')
    header_content = SerializerMethodField('get_header_text')
    like_count = SerializerMethodField('get_like_count')
    comment_count = SerializerMethodField('get_comment_count')
    user = UserListSerializer()

    class Meta:
        model = Article
        fields = [
            'id',
            'user',
            'create_date',
            'header',
            'header_media',
            'header_content',
            'like_count',
            'comment_count'
        ]

    def get_header_media(self, obj: Article):
        #print(obj.content)
        media_block = None
        for block in obj.content:
            #print(block)
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
            
    def get_like_count(self, obj: Article) -> int:
        return obj.api_articlelike.count()
    
    def get_comment_count(self, obj: Article) -> int:
        return obj.api_comment.count()


