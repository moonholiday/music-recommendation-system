from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from django.http import HttpResponseRedirect
import sys
from .models import *

client_id="b4dad3bdf5144e6f8f408ec2f6f278a3"
client_secret="a1e9ff23036a4444abcf6067fd63c2ca"

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class FaqPageView(TemplateView):
    template_name = 'faq.html'

def GenrePageView(request):
    sp = spotipy.Spotify(auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))
    genres = sp.categories()
    new = []
    for idx, genre  in enumerate(genres['categories']['items']):
        new += (idx, genre['name'])
        print(new)

    context = {'genre_list': new}
    return render(request, 'genre.html', context = context)

def discover(request):
    query = request.POST.get('q')
    if request.method=='POST':
        sp = spotipy.Spotify(auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))
        result = sp.search(q=query, limit=20)
        new = []

        for idx, track in enumerate(result['tracks']['items']):
            new += (idx, track['name'])

        print(new)
        return render(request, 'discover.html', {'result': new})
    else:
        return render(request, 'discover.html')

# category list view
def free_music(request):
    # display all genres
    categories = Category.objects.all()

    context = {
        'categories': categories
    }
    return render(request, 'free_music.html', context=context)

# song list view of each category
def single_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    songs = Song.objects.filter(category=category)
    context = {
        'category': category,
        'songs': songs,
    }

    return render(request, 'single_category.html', context=context)
