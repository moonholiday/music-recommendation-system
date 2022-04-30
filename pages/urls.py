from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('genre/', views.GenrePageView, name='genre'),
    path('discover/', views.discover, name='discover'),
    path('free_music/', views.free_music, name='free_music'),
    path('add_music/', views.add_music, name='add_music'),
    path('<slug:slug>', views.single_category, name='single_category'),
    path('update_music/<int:pk>/', views.update_music, name='update_music'),
    path('delete_music/<int:pk>/', views.delete_music, name='delete_music'),
    path('', HomePageView.as_view(), name='home'),
]
