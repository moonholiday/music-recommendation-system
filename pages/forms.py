from dataclasses import field
from django import forms
from .models import Song
from django.contrib.auth.models import User

class AudioForm(forms.ModelForm):
    class Meta:
        model = Song
        fields =  ['name', 'category', 'song_img', 'artist', 'song_file']
