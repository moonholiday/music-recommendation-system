from django.shortcuts import render, redirect
from django.views.generic import TemplateView
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from django.http import HttpResponseRedirect
import sys

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class FaqPageView(TemplateView):
    template_name = 'faq.html'

def discover(request):
    query = request.POST.get('q')
    if request.method=='POST':
        sp = spotipy.Spotify(auth_manager = SpotifyClientCredentials(client_id="b4dad3bdf5144e6f8f408ec2f6f278a3", client_secret="a1e9ff23036a4444abcf6067fd63c2ca"))
        result = sp.search(q=query, limit=10)
        new = []

        for idx, track in enumerate(result['tracks']['items']):
            new += (idx, track['name'])
            
        print(new)
        return render(request, 'discover.html', {'result': new})
    else:
        return render(request, 'discover.html')



class FreemusicPageView(TemplateView):
    template_name = 'freemusic.html'

class GenrePageView(TemplateView):
    template_name = 'genre.html'
