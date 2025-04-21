import json
from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.exceptions import ValidationError
#from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from .services.article import *
from .services.author import *
from .services.auth import *
from .serializers import *
from .models import *


# Create your views here.
class TestAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request: Request):
        #print(request.headers.get('Authorization'))
        return Response({"response": "get"})
    
    def post(self, request: Request):
        print(request.data)
        from random import randint
        return Response({"response": randint(1, 10)})

class MediaView(ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer

class ArticleView(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    #call it before accessing edit menu of an article
    def get(self, request: Request, id: int): 
        user = request.user
        article_obj = self.queryset.get(pk=id)
        serializer = self.serializer_class(article_obj)

        is_owner = article_obj.author == user
        res_data = dict(serializer.data)
        res_data['is_owner'] = is_owner

        return Response(res_data, status=200)
            
    #object already exists (can't access /article/edit if it doesn't), so no need tto do checks
    def save(self, request: Request): 
        id = request.data.get('id') #PATCH request, so no need to pass id as argument
        new_text_content = request.data.get('text_content')

        article_obj = self.queryset.get(pk=id) #its ensured that such object already exists
        
        serializer = self.serializer_class(
            article_obj,
            data={
                'text_content': new_text_content
            },
            partial=True
        ) 
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Saved successfully!'}, status=200)
        else:
            return Response({"message": serializer.errors}) #TODO: errors handling
        
    #save & set is_published = True
    def publish(self, request: Request):
        id = request.data.get('id') #PATCH request, so no need to pass id as argument
        new_text_content = request.data.get('text_content')
        #PUBLISH status??? Subject to change

        article_obj = self.queryset.get(pk=id)

        serializer = self.serializer_class(
            article_obj,
            data={
                'text_content': new_text_content,
                'is_published': True,
            },
            partial=True
        ) 
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Published successfully!'}, status=200)
        else:
            return Response({"message": serializer.errors}) #TODO: errors handling

class UserView(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request: Request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer) 
        else:
            return Response({'message': serializer.errors})
        
        headers = self.get_success_headers(serializer.data)
        token_pair = obtain_pair(request.data)
        
        return Response(token_pair, status=status.HTTP_201_CREATED, headers=headers)


    def decode_user_data(self, request: Request):
        access_token = request.data.get('access')
        try:
            user = decode_access(access_token)
        except TokenError:
            return Response({"message": "Access token is invalid!"}, status=502)
    
        serializer = self.serializer_class(user)
        return Response(serializer.data)




"""
class ArticleView(ViewSet):
    def list(self, request):
        data = article_list()
        data_S = ArticleSerializer(data, many=True)
        return data_S.data
    
    def create(self, validated_data):
"""

