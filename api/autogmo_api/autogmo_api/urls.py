"""autogmo_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from decouple import config
from django.contrib import admin
from django.settings import API_URL_BASE
from django.urls import include, path

urlpatterns = [
    path(f"{API_URL_BASE}" + r"admin/", admin.site.urls),
    path(f"{API_URL_BASE}", include("apps.auth.urls")),
]

if config("DEBUG", default=True, cast=bool):
    urlpatterns = [
        path(f"{API_URL_BASE}" + r"__debug__/", include("debug_toolbar.urls")),
    ] + urlpatterns