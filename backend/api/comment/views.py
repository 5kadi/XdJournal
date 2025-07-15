from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.request import Request
from rest_framework.response import Response
from .serializers import *
from .models import Comment
from .pagination import CommentPaginator

class CommentView(ModelViewSet):
    queryset = Comment.objects.all().reverse() #newest comments should be first (temporary)
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def list(self, request: Request, article_id: int, *args, **kwargs):
        sel_comments = self.queryset.filter(article__pk=article_id)
        paginated_comments = CommentPaginator.paginate_queryset(sel_comments, request)
        serializer = CommentURDListSerializer(
            paginated_comments, 
            custom_kwargs={ "request_user": request.user },
            many=True
        )

        return CommentPaginator.get_paginated_response(serializer.data)
    
    def create(self, request: Request, article_id: int, *args, **kwargs):
        comment_data = request.data
        comment_data['user'] = request.user.id
        comment_data['article'] = article_id
        #print(comment_data)

        serializer = self.serializer_class(data=comment_data)
        if serializer.is_valid():
            self.perform_create(serializer)
            #data instead of validated_data, because validated_data returns user & article as an object
            #Also no need for message field lmao
            return Response({'message': 'Created a comment successfully!', **serializer.data}, status=201)
        else:
            return Response({'message': serializer.errors}, status=400)