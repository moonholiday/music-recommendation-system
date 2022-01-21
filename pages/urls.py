from django.urls import path
from .views import HomePageView, AboutPageView, FaqPageView, GenrePageView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('faq/', FaqPageView.as_view(), name='faq'),
    path('genre/', GenrePageView.as_view(), name='genre'),
    path('', HomePageView.as_view(), name='home'),
]
