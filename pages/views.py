from django.shortcuts import render, redirect
from django.views.generic import TemplateView
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from django.http import HttpResponseRedirect
import sys
from .models import *

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class FaqPageView(TemplateView):
    template_name = 'faq.html'

class GenrePageView(TemplateView):
    template_name = 'genre.html'

def discover(request):
    query = request.POST.get('q')
    if request.method=='POST':
        sp = spotipy.Spotify(auth_manager = SpotifyClientCredentials(client_id="b4dad3bdf5144e6f8f408ec2f6f278a3", client_secret="a1e9ff23036a4444abcf6067fd63c2ca"))
        result = sp.search(q=query, limit=20)
        new = []

        for idx, track in enumerate(result['tracks']['items']):
            new += (idx, track['name'])

        print(new)
        return render(request, 'discover.html', {'result': new})
    else:
        return render(request, 'discover.html')

def free_music(request):
    # display all genres
    genres = Genre.objects.all()

    context = {
        'genres': genres
    }
    return render(request, 'free_music.html', context=context)

def player(request, genre_id):
    songs = Song.objects.all()
    genres = Genre.objects.filter(id=genre_id).first()
    context = {
        'genres': genres,
        'songs': songs,
    }
    return render(request, 'player.html', context=context)

def CategoryView(request, gen):
    category_songs = Song.objects.filter(genre=gen)
    context = {
        'gen': gen,
        'category_songs': category_songs,
    }


    return render(request, 'categories.html', context=context)
