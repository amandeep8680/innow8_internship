from django.db import models

# Create your models here.
class profiles(models.Model):
    name = models.CharField(max_length=25)
    age = models.IntegerField(null=True)
    email = models.EmailField(null=True)
    
    def __str__(self):
        return self.name
        