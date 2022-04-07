from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=120)


class Track(models.Model):
    title = models.CharField(max_length=120)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)


class User(models.Model):
    email = models.CharField(max_length=120)


class Download(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)
