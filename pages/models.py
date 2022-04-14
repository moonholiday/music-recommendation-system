from django.db import models

class Song(models.Model):
    Genre_Option = (
        ('Happy', 'Happy'),
        ('Cinematic', 'Cinematic'),
        ('Games', 'Games'),
        ('Calm', 'Calm'),
        ('Vlog', 'Vlog'),
    )

    name=models.CharField(max_length=200)
    genre=models.CharField(max_length=20,choices=Genre_Option,default='Happy')
    song_img=models.FileField()
    artist=models.CharField(max_length=200)
    song_file=models.FileField()

    def __str__(self):
        return self.name

class Genre(models.Model):
    name=models.CharField(max_length=200)
    genre_img=models.FileField()

    def __str__(self):
        return self.name
