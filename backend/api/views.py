
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.exceptions import ValidationError
from rest_framework.parsers import MultiPartParser
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

        is_owner = article_obj.author == user

        return Response({"is_owner": is_owner, **serializer.data}, status=200)
    
    def list(self, request: Request):
        serializer = ArticleListSerializer(self.queryset[:5], many=True) #boilerplate
        return Response(serializer.data, status=200)
            
    #object already exists (can't access /article/edit if it doesn't), so no need tto do checks
    def save_block(self, request: Request, id: int): 
        content_frag = request.data.get('content_frag')
        article_obj = self.queryset.get(pk=id)

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

class ArticleMediaView(ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = ArticleMediaSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request: Request, id: int):
        media_data = request.data
        media_data["author"] = request.user.id
        media_data["article"] = id
        article_obj = Article.objects.get(pk=id)

        if not check_ownership(article_obj, request.user):
            return Response({"message": "You don't own this article!"}, status=401)

        serializer = self.serializer_class(data=media_data)
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
        
        return Response(
            {"message": "Created an account successfully!", **token_pair}, 
            status=status.HTTP_201_CREATED, 
            headers=headers
        )

    def decode_user_data(self, request: Request):
        access_token = request.data.get('access')
        try:
            user = decode_access(access_token)
        except TokenError:
            return Response({"message": "Access token is invalid!"}, status=502)
    
        serializer = self.serializer_class(user)
        return Response(serializer.data)

class CustomTokenObtainPairView(TokenObtainPairView):
        permission_classes = [AllowAny]
        
        def post(self, request: Request, *args, **kwargs) -> Response:
            serializer = self.get_serializer(data=request.data)

            if serializer.is_valid(raise_exception=True):
                return Response({"message": "Logged in successfully!", **serializer.validated_data}, status=200)
            else:
                return Response({"message": serializer.errors}, status=400)


"""
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
"""


"""
class ArticleView(ViewSet):
    def list(self, request):
        data = article_list()
        data_S = ArticleSerializer(data, many=True)
        return data_S.data
    
    def create(self, validated_data):
"""

