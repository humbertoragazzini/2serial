"""
Home urls
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.serial_generator, name='serial_generator')
]
