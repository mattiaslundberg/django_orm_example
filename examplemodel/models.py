from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return f"Artist {self.name}"


class Track(models.Model):
    title = models.CharField(max_length=120)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return f"Track {self.title}"


class User(models.Model):
    email = models.CharField(max_length=120)

    def __str__(self):
        return self.email


class Download(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)
