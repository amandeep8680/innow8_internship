from django.db import models

# Create your models here.
class Info(models.Model):
    name = models.CharField(max_length=25)
    age = models.IntegerField(default=18)
    messege = models.CharField(max_length=100,default="No Messege")


def __str__(self):
    return self.name