from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()


class Album(models.Model):
    title = models.CharField(max_length=50, verbose_name='Title')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Picture(models.Model):
    title = models.CharField(max_length=50, verbose_name='Title')
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True, blank=True)
    image = models.FileField(upload_to='pictures')

    def __str__(self):
        return self.title
