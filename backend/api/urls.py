from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path, include



urlpatterns = [
    path(r'article/', include('api.article.urls')),
    path(r'auth/', include('api.auth.urls')),
    path(r'media/', include('api.media.urls')),
    path(r'comment/', include('api.comment.urls')),
    path(r'like/', include('api.like.urls'))
]