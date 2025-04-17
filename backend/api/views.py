import json
from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
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
from .services.user import *
from .services.auth import *
from .serializers import *
from .models import *


# Create your views here.
class TestAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        #print(request.headers.get('Authorization'))
        return Response({"response": "get"})
    
    def post(self, request):
        print(request.data)
        from random import randint
        return Response({"response": randint(1, 10)})

class MediaView(ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer

class ArticleView(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]

    #object already exists (can't access /article/edit if it doesn't), so no need tto do checks
    def save(self, request): 
        id = request.data.get('id')
        new_text_content = request.data.get('text_content')

        article_obj = self.queryset.get(pk=id)
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
            return Response(serializer.errors) #TODO: errors handling


class UserView(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True) #questionable
        self.perform_create(serializer) 
        
        headers = self.get_success_headers(serializer.data)
        token_pair = obtain_pair(request.data)
        
        return Response(token_pair, status=status.HTTP_201_CREATED, headers=headers)


    def decode_user_data(self, request):
        access_token = request.data.get('access')
        user = decode_access(access_token)
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

