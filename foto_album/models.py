from django.db import models
from django.contrib.auth.models import User


class Album(models.Model):
    title = models.CharField(max_length=50, verbose_name='Title')
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Picture(models.Model):
    title = models.CharField(max_length=50, verbose_name='Title')
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
