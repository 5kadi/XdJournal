from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.request import Request
from rest_framework.response import Response
from api.services import check_ownership, ownership_required
from .serializers import *
from .models import Article
from .services import *


class ArticleView(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def create(self, request: Request):
        article_data = request.data
        article_data['user'] = request.user.id

        serializer = self.serializer_class(data=article_data)
        if serializer.is_valid():
            self.perform_create(serializer)
            #data instead of validated_data, because validated_data returns user as an object
            #Also no need for message field lmao
            return Response({'message': 'Created an article successfully!', **serializer.data}, status=201)
        else:
            return Response({'message': serializer.errors}, status=400)

    #call it before editing an article
    def get(self, request: Request, id: int): 
        user = request.user
        article_obj = get_object_or_404(self.queryset, pk=id)
        serializer = self.serializer_class(article_obj)

        return Response(
            {
                "is_owner": article_obj.user == user, 
                **serializer.data
            }, 
            status=200
        )
    
    def list(self, request: Request):
        serializer = ArticleListSerializer(self.queryset.filter(is_published=True), many=True) #boilerplate
        return Response(serializer.data, status=200)
            
    #object already exists (can't access /article/edit if it doesn't), so no need tto do checks
    @ownership_required()
    def save_block(self, request: Request, id: int, *args, **kwargs): 
        article_obj = kwargs.get('sel_obj')
        block_id = int(request.data.get('block_id'))
        block = request.data.get('block')

        if block_is_valid(block):
            modify_content(article_obj, block_id, block)
            return Response({'message': 'Saved successfully!'}, status=200) #message is useless here Xd
        else:
            return Response({"message": "Invalid JSON schema!"}, status=400)
        
    @ownership_required()
    def delete_block(self, request: Request, id: int, *args, **kwargs):
        article_obj = kwargs.get('sel_obj')
        block_id = int(request.data.get('block_id'))
        block = pop_block(article_obj, block_id)
        if not block:
            return Response({"message": "Article should have at least 1 block!"}, status=400)
        else:
            return Response({"message": "Deleted block successfully!"}, status=400)

    #save & set is_published = True
    @ownership_required()
    def publish(self, request: Request, id: int, *args, **kwargs):
        article_obj = kwargs.get('sel_obj')
        publish_status: bool = request.data.get('publish_status')

        serializer = self.serializer_class(
            article_obj,
            data={
                'is_published': publish_status,
            },
            partial=True
        ) 
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Published successfully!'}, status=200)
        else:
            return Response({"message": serializer.errors}, status=400) #idk what code to choose lmao, TODO: errors handling