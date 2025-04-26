import json
from django.shortcuts import render, get_object_or_404
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
from .utils.model_utils import *
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

    def create(self, request: Request):
        article_data = request.data
        article_data['author'] = request.user.id

        serializer = self.serializer_class(data=article_data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=200)
        else:
            return Response({'message': serializer.errors}, status=400)

    #call it before accessing edit menu of an article
    def get(self, request: Request, id: int): 
        user = request.user
        article_obj = get_object_or_404(self.queryset, pk=id)
        serializer = self.serializer_class(article_obj)

        is_owner = article_obj.author == user
        res_data = dict(serializer.data)
        res_data['is_owner'] = is_owner

        return Response(res_data, status=200)
            
    #object already exists (can't access /article/edit if it doesn't), so no need tto do checks
    def save(self, request: Request): 
        id = request.data.get('id') #PATCH request, so no need to pass id as argument
        new_content = request.data.get('content')
        header = request.data.get('header')

        article_obj = self.queryset.get(pk=id) #its ensured that such object already exists
        
        serializer = self.serializer_class(
            article_obj,
            data={
                'content': new_content,
                'header': header
            },
            partial=True
        ) 
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Saved successfully!'}, status=200)
        else:
            return Response({"message": serializer.errors}, status=400) #TODO: errors handling
        
    #save & set is_published = True
    def publish(self, request: Request):
        id = request.data.get('id') #PATCH request, so no need to pass id as argument
        new_content = request.data.get('content')
        header = request.data.get('header')
        #PUBLISH status??? Subject to change

        article_obj = self.queryset.get(pk=id) #it's already ensured that object exists

        serializer = self.serializer_class(
            article_obj,
            data={
                'content': new_content,
                'header': header,
                'is_published': True,
            },
            partial=True
        ) 
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Published successfully!'}, status=200)
        else:
            return Response({"message": serializer.errors}, status=400) #idk what code to choose lmao, TODO: errors handling

class MediaView(ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request: Request, *args, **kwargs):
        media_data = request.data
        media_data['author'] = request.user.id

        serializer = self.serializer_class(data=media_data)
        if serializer.is_valid():
            self.perform_create(serializer)
            push_content(media_data["article"], serializer.data["content"])
            res_data = dict(serializer.data)
            res_data["message"] = "Uploaded successfully. Don't forget to save changes before refreshing the page!"
            return Response(res_data, status=200)
        else:
            return Response({'message': serializer.errors}, status=400)


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

