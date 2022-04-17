from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('genre/', views.GenrePageView, name='genre'),
    path('discover/', views.discover, name='discover'),
    path('free_music/', views.free_music, name='free_music'),
    path('<slug:slug>', views.single_category, name='single_category'),
    path('', HomePageView.as_view(), name='home')
]
