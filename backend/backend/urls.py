"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from api import urls
from .settings import MEDIA_ROOT, MEDIA_URL
from .views import custom_404_view
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('api/', include('api.urls'))
] + static(MEDIA_URL, document_root=MEDIA_ROOT)

handler404 = custom_404_view
