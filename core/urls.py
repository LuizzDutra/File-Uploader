from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainPage.index, name='index'),
    path('serving', views.MainPage.get_servings, name='serving')
]
