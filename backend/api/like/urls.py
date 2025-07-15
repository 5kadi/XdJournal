from django.urls import path, include
from .views import *

urlpatterns = [
    path(r"<slug:obj_type>/<int:obj_id>/set", LikeView.as_view({"post": "set_like"})),
    path(r"<slug:obj_type>/<int:obj_id>/remove", LikeView.as_view({"delete": "remove_like"})),
]