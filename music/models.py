from django.db import models
from django.core.urlresolvers import reverse

class Album(models.Model):
    artist = models.CharField(max_length=100)
    album_title = models.CharField(max_length=100)
    genre = models.CharField(max_length=10)
    album_logo = models.FileField()


    def __str__(self):
        return self.artist + '-' + self.album_title

    def get_absolute_url(self):
        return reverse('music:detail' , kwargs={'pk':self.pk})

class Song(models.Model):
    album = models.ForeignKey(Album , on_delete=models.CASCADE)
    song_title = models.CharField(max_length=500)
    file_type = models.CharField(max_length=10)
    is_favorite = models.BooleanField(default=False)


    def __str__(self):
        return self.song_title