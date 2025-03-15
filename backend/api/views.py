import json
from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import status
#from rest_framework.
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.exceptions import ValidationError
#from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
#from rest_framework_simplejwt.authentication import a
from .services.article import *
from .services.user import *
from .services.auth import obtain_pair
from .serializers import *
from .models import *


# Create your views here.
class TestAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        print(request.headers)
        return Response({"response": "get"})
    
    def post(self, request):
        print(request.POST)
        return Response({"response": "post"})


class MediaView(ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer

class ArticleView(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class UserView(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        headers = self.get_success_headers(serializer.data)
        token_pair = obtain_pair(request.data)
        
        return Response(token_pair, status=status.HTTP_201_CREATED, headers=headers)


    def decode_user_data(self, request):
        user = decode_access(request)
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

