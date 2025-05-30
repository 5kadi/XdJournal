from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path, include
from .views import *


urlpatterns = [
    path(r"test", TestAPIView.as_view()),

    path(r"user/list", UserView.as_view({'get': 'list'})),
    path(r"user/create", UserView.as_view({'post': 'create'})),
    path(r"user/token/get", CustomTokenObtainPairView.as_view()),
    path(r"user/token/refresh", TokenRefreshView.as_view()),
    path(r"user/token/data", UserView.as_view({'post': 'decode_user_data'})),


    path(r"article/get/<int:id>", ArticleView.as_view({'get': 'get'})),
    path(r"article/list", ArticleView.as_view({'get': 'list'})),
    path(r"article/create", ArticleView.as_view({'post': 'create'})),
    path(r"article/<int:id>/save_block", ArticleView.as_view({'patch': 'save_block'})),
    path(r"article/<int:id>/publish", ArticleView.as_view({'patch': 'publish'})),

    path(r"article/<int:id>/media/create", ArticleMediaView.as_view({'post': 'create'})),
    #path(r"article/<int:id>/media/list", ArticleMediaView.as_view({'get': 'list'})),
]