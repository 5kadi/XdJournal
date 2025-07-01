from django.core.files.uploadedfile import InMemoryUploadedFile
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from api.services import check_ownership, ownership_required
from api.article.services import insert_block, pop_block, modify_content
from .models import Media, ArticleMedia
from .serializers import *
from .services import *


class ArticleMediaView(ModelViewSet):
    queryset = ArticleMedia.objects.all()
    serializer_class = ArticleMediaSerializer
    permission_classes = [IsAuthenticated]

    @ownership_required(model=Article)
    def create(self, request: Request, id: int, *args, **kwargs):
        article_obj = kwargs.get('sel_obj')      
        block_id = int(request.data.get('block_id'))
        media_data = {
            "user": request.user.id,
            "article": id,
            "content": request.data.get("block_content")
        }

        serializer = self.serializer_class(data=media_data)
        if serializer.is_valid():
            #serializer.validated_data["content"] = parse.unquote_plus(serializer.validated_data["content"])
            self.perform_create(serializer)

            modify_content(article_obj, block_id, {"type": "media", "content": serializer.data["content"]})
            return Response(serializer.data, status=200)
        else:
            return Response({'message': serializer.errors}, status=400)
        
    @ownership_required(model=Article)
    def delete(self, request: Request, id: int, *args, **kwargs):
        article_obj = kwargs.get('sel_obj')     
        block_id = int(request.data.get('block_id'))
        media_block = pop_block(article_obj, block_id)
        if not media_block:
            return Response({"message": "Article should have at least 1 block!"}, status=400)
        
        media_obj = get_by_content(article_obj, media_block["content"])
        if not media_obj:
            insert_block(article_obj, block_id, media_block)
            return Response({"message": "Server Error: Object doesn't exist!"}, status=400) #lmao
        
        media_obj.delete()

        return Response({"message": "Deleted media successfully!"}, status=200) #useless message btw
