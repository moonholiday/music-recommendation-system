from django.db import models
from django.utils.text import slugify
from .helpers import get_audio_length
from .validators import validate_is_audio
from django.contrib.auth.models import User

class Song(models.Model):
    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    name=models.CharField(max_length=200)
    category=models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)
    song_img=models.FileField()
    artist=models.CharField(max_length=200)
    time_length=models.DecimalField(null=True, max_digits=20, decimal_places=2,blank=True)
    song_file=models.FileField(validators=[validate_is_audio])
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True ,blank=True)
    favourites = models.ManyToManyField(User, related_name='favourite', default=None, blank=True)
    status = models.CharField(max_length=10, choices=options, default='draft')

    objects = models.Manager()
    newmanager = NewManager()

    def __str__(self):
        return self.name
    def save(self,*args, **kwargs):
        if not self.time_length:
            # logic for getting length of audio
            audio_length=get_audio_length(self.song_file)
            self.time_length =f'{audio_length:.2f}'

        return super().save(*args, **kwargs)

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
