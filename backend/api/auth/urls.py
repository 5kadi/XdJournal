from django.urls import path, include
from .views import *

urlpatterns = [
    path(r"list", UserView.as_view({'get': 'list'})),
    path(r"create", UserView.as_view({'post': 'create'})),
    path(r"data", UserView.as_view({"get": "refresh_user_data"})),
    path(r"update/<int:id>", UserView.as_view({"patch": "patch_user_data"})),
    path(r"token/get", CustomTokenObtainPairView.as_view()),
    path(r"token/refresh", TokenRefreshView.as_view()),
]

