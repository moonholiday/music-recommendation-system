from django.shortcuts import render, redirect
from django.views.generic import TemplateView
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from .models import Editors

# Creating views
class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = Editors.objects.all()
        return context



class AboutPageView(TemplateView):
    template_name = 'about.html'

class FaqPageView(TemplateView):
    template_name = 'faq.html'

class GenrePageView(TemplateView):
    template_name = 'genre.html'
    sp = spotipy.Spotify(auth_manager = SpotifyClientCredentials(client_id="b4dad3bdf5144e6f8f408ec2f6f278a3", client_secret="a1e9ff23036a4444abcf6067fd63c2ca"))
    result = sp.search(q="bipul chettri", limit=40)
    new = []
    for idx, track in enumerate(result['tracks']['items']):
        print(idx, track['name'])
