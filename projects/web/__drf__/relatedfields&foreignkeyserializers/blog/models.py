from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Album(models.Model):
    name = models.CharField(max_length = 25)

    def __str__ (self):
        return self.name



class Track(models.Model):
    album =models.ForeignKey(Album , related_name='tracks', on_delete=models.CASCADE)
    title = models.CharField(max_length=35)     
    def __str__(self):
        return self.title
