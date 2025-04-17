from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path, include
from .views import *


urlpatterns = [
    path(r"test", TestAPIView.as_view()),

    path(r"user/list", UserView.as_view({'get': 'list'})),
    path(r"user/create", UserView.as_view({'post': 'create'})),
    path(r"user/token/get", TokenObtainPairView.as_view()),
    path(r"user/token/refresh", TokenRefreshView.as_view()),
    path(r"user/token/data", UserView.as_view({'post': 'decode_user_data'})),


    path(r"article/get/<int:pk>", ArticleView.as_view({'get': 'retrieve'})),
    path(r"article/list", ArticleView.as_view({'get': 'list'})),
    path(r"article/create", ArticleView.as_view({'post': 'create'})),
    path(r"article/save", ArticleView.as_view({'patch': 'save'})),

    path(r"media/create", MediaView.as_view({'post': 'create'})),
    path(r"media/list", MediaView.as_view({'get': 'list'})),
]