from rest_framework.serializers import ModelSerializer, SerializerMethodField
from api.auth.serializers import UserListSerializer
from .models import Comment

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

class CommentListSerializer(ModelSerializer):
    user = UserListSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = [
            "user",
            "create_date",
            "update_date",
            "content"
        ]