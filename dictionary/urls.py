from django.urls import path,include
from django.contrib import admin
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('word', views.word, name='word'),
    path('accounts/', include("django.contrib.auth.urls")),
    path('user/', include('user.urls')),
]