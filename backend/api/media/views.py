from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import Media, ArticleMedia
from .serializers import *
from api.services import check_ownership
from .services import *


class ArticleMediaView(ModelViewSet):
    queryset = ArticleMedia.objects.all()
    serializer_class = ArticleMediaSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request: Request, id: int):
        request.data["user"] = request.user.id
        request.data["article"] = id
        article_obj = Article.objects.get(pk=id)

        if not check_ownership(article_obj, request.user):
            return Response({"message": "You don't own this article!"}, status=401)

        print(request.data)

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            
            frag_content = {
                "type": "media",
                "content": serializer.data["content"]
            }
            push_content(article_obj, serializer.data["frag_id"], frag_content)
            
            return Response({'message': 'Created an article successfully!', **serializer.data}, status=200)
        else:
            return Response({'message': serializer.errors}, status=400)