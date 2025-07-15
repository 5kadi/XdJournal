from rest_framework.serializers import ModelSerializer, SerializerMethodField
from api.serializers import ReadOnlyModelSerializer, CustomKwargsMixin
from api.auth.serializers import UserListSerializer
from .models import Comment

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class CommentListSerializer(ReadOnlyModelSerializer):
    like_count = SerializerMethodField('get_like_count')
    user = UserListSerializer()

    class Meta:
        model = Comment
        fields = [
            "id",
            "user",
            "create_date",
            "update_date",
            "content",
            "like_count",
        ]

    def get_like_count(self, obj: Comment) -> int:
        return obj.api_commentlike.count()

#URD = user related data Xd
class CommentURDListSerializer(CommentListSerializer, CustomKwargsMixin):
    is_owner = SerializerMethodField('get_is_owner')
    is_liked = SerializerMethodField('get_is_liked')
    
    class Meta:
        model = Comment
        fields = [
            "id",
            "user",
            "create_date",
            "update_date",
            "content",
            "like_count",
            "is_owner",
            "is_liked"
        ]
    
    def get_is_owner(self, obj: Comment) -> bool:
        request_user = self.custom_kwargs["request_user"]
        return request_user == obj.user
    
    def get_is_liked(self, obj: Comment) -> bool:
        request_user = self.custom_kwargs["request_user"]
        #print(obj.api_commentlike.all())
        return bool(obj.api_commentlike.filter(user=request_user.id).count())

