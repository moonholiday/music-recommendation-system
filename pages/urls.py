from django.urls import path
from .views import HomePageView, AboutPageView, FaqPageView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('faq/', FaqPageView.as_view(), name='faq'),
    path('', HomePageView.as_view(), name='home'),
]
