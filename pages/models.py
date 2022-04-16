from django.db import models

class Song(models.Model):

    name=models.CharField(max_length=200)
    category=models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)
    song_img=models.FileField()
    artist=models.CharField(max_length=200)
    song_file=models.FileField()

    def __str__(self):
        return self.name

class Category(models.Model):
    name=models.CharField( max_length=200)
    category_img=models.FileField()

    class Meta:
        verbose_name_plural = 'categories'


    def __str__(self):
        return self.name
