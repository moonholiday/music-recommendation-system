from django.urls import path
from .views import *

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('faq/', FaqPageView.as_view(), name='faq'),
    path('genre/', GenrePageView.as_view() , name='genre'),
    path('discover/', DiscoverPageView.as_view() , name='discover'),
    path('freemusic/', FreemusicPageView.as_view() , name='freemusic'),
    path('', HomePageView.as_view(), name='home'),
]
