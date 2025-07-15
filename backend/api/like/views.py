from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from api.article.models import Article
from api.comment.models import Comment
from .serializers import *
from .models import *

class LikeView(ViewSet):
    permission_classes = [IsAuthenticated]
    models = {
        "article": [Article, ArticleLike],
        "comment": [Comment, CommentLike]
    }

    def set_like(self, request: Request, obj_type: str, obj_id: int, *args, **kwargs):
        obj_model = self.models[obj_type][0]
        like_model = self.models[obj_type][1]

        like_data = {
            "user": request.user,
            obj_type: get_object_or_404(obj_model, pk=obj_id)
        }

        try:
            like_model.objects.get(**like_data) 
        except ObjectDoesNotExist:
            like = like_model.objects.create(**like_data)
            like.save()
            return Response({"message": f"Liked {obj_type} successfully!"}, status=201)
        else:
            return Response({"message": f"This {obj_type} is already liked!"}, status=400)

        
    def remove_like(self, request: Request, obj_type: str, obj_id: int, *args, **kwargs):
        obj_model = self.models[obj_type][0]
        like_model = self.models[obj_type][1]

        like_data = {
            "user": request.user,
            obj_type: get_object_or_404(obj_model, pk=obj_id)
        }
        like = get_object_or_404(like_model, **like_data)
        like.delete()
        
        return Response({"message": "Removed like successfully!"}, status=200)

        
