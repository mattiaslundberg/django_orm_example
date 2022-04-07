from django.db import models


class User(models.Model):
    email = models.CharField(max_length=120, db_index=True)


class Download(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)

    class Meta:
        indexes = [models.Index(fields=["user", "track"])]


class Artist(models.Model):
    name = models.CharField(max_length=120, unique=True)
