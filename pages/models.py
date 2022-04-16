from django.db import models
from django.utils.text import slugify

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
    slug = models.SlugField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
