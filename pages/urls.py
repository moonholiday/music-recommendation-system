from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('genre/', views.GenrePageView, name='genre'),
    path('genre_playlist/', views.genre_playlist, name='genre_playlist'),
    path('discover/', views.discover, name='discover'),
    path('free_music/', views.free_music, name='free_music'),
    path('add_music/', views.add_music, name='add_music'),
    path('<slug:slug>', views.single_category, name='single_category'),
    path('', HomePageView.as_view(), name='home'),
]
