from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.request import Request
from rest_framework.response import Response
from api.services import check_ownership
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

    #call it before accessing edit menu of an article
    def get(self, request: Request, id: int): 
        user = request.user
        article_obj = get_object_or_404(self.queryset, pk=id)
        serializer = self.serializer_class(article_obj)

        is_owner = article_obj.user == user

        return Response({"is_owner": is_owner, **serializer.data}, status=200)
    
    def list(self, request: Request):
        serializer = ArticleListSerializer(self.queryset[:5], many=True) #boilerplate
        return Response(serializer.data, status=200)
            
    #object already exists (can't access /article/edit if it doesn't), so no need tto do checks
    def save_block(self, request: Request, id: int): 
        content_frag = request.data.get('content_frag')
        article_obj = self.queryset.get(pk=id)
        print(content_frag)

        if not check_ownership(article_obj, request.user):
            return Response({"message": "You don't own this article!"}, status=401)

        if content_frag_is_valid(content_frag):
            frag_id, frag_content = [*content_frag.items()][0]
            push_content(article_obj, frag_id, frag_content)
            return Response({'message': 'Saved successfully!'}, status=200)
        else:
            return Response({"message": "Invalid JSON schema!"}, status=400)
        
    #save & set is_published = True
    def publish(self, request: Request, id: int):
        publish_status: bool = request.data.get('publish_status')
        article_obj = self.queryset.get(pk=id) #it's already ensured that object exists

        if not check_ownership(article_obj, request.user):
            return Response({"message": "You don't own this article!"}, status=401)

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