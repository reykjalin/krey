from django.db import models

# Create your models here.
class Torrent(models.Model):
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=32)
    percent = models.IntegerField(default = 0)
