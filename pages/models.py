from django.db import models

class Song(models.Model):
    # genre_option = Genre.filter(name= name)
    # genre_list = []
    # for item in genre_option:
    #     genre_list.append(item)

    genre_list = (
        ('happy', 'happy'),
        ('cinematic', 'cinematic'),
        ('games', 'games'),
        ('calm', 'calm'),
        ('vlog', 'vlog'),
    )

    # genre_obj = models.ForeignKey('Genre', on_delete=models.CASCADE)
    # @property
    # def genreName(self):
    #     return self.genre_obj.name

    name=models.CharField(max_length=200)
    genre=models.CharField(max_length=20,choices=genre_list,default='happy')
    song_img=models.FileField()
    artist=models.CharField(max_length=200)
    song_file=models.FileField()

    def __str__(self):
        return self.name

class Genre(models.Model):
    name=models.CharField( max_length=200)
    genre_img=models.FileField()

    def __str__(self):
        return self.name
