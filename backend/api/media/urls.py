from django.urls import path, include
from .views import *


urlpatterns = [
    path(r"article/<int:id>/create", ArticleMediaView.as_view({'post': 'create'})),
    path(r"article/<int:id>/delete", ArticleMediaView.as_view({'delete': 'delete'})),
]