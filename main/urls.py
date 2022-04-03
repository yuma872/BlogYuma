from os import abort
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('aboutme/', views.aboutme, name='aboutme')
]
