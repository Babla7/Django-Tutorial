from django.contrib import admin
from django.urls import path
from life import views

urlpatterns = [
    path('', views.index, name = 'home') #Connect to Views file
]
