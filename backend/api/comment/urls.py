from django.urls import path, include
from .views import *

urlpatterns = [
    path(r"<int:article_id>/list", CommentView.as_view({"get": "list"})),
    path(r"<int:article_id>/create", CommentView.as_view({"post": "create"})),
]