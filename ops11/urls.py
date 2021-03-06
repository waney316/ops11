"""ops11 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include, re_path

from apps.book import urls as book_urls
from rest_framework import routers
from rest_framework.authtoken import views
from rest_framework_jwt.views import verify_jwt_token, refresh_jwt_token, obtain_jwt_token
from apps.book.router import book_router

router = routers.DefaultRouter()
router.registry.extend(book_router.registry)

API_URLS = []
API_URLS.extend(book_urls.urlpatterns)
API_URLS.extend(router.urls)
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', include(book_urls)),
    # path('api/', include(router.urls)),
    path('api/', include(API_URLS)),

    # register drf router

    # api-auth=token
    # path('api-token-auth/', views.obtain_auth_token),

    # JWT
    re_path(r'^api-token-verify/', verify_jwt_token),
    re_path(r'^api-token-auth/', obtain_jwt_token),
    re_path(r'^api-token-refresh/', refresh_jwt_token),
]

