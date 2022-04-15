from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('genre/', GenrePageView.as_view(), name='genre'),
    path('discover/', views.discover, name='discover'),
    path('free_music/', views.free_music, name='free_music'),
    path('songs/<int:genre_id>/', views.player, name='songs'),
    path('category/<str:gen>/', CategoryView, name='category'),
    path('', HomePageView.as_view(), name='home')
]
