from django.contrib import admin
from django.urls import path
from . import apis

urlpatterns = [
    path('api/images', apis.ImageApi.as_view(), name="ImageApi")
]
