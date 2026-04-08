from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=10)
    age = models.IntegerField()
    email = models.EmailField(unique=True,)
    company = models.CharField(max_length=25,default="Innow8")
    city = models.CharField(max_length=10,default="unknown")


    def __str__(self):
        return self.name
