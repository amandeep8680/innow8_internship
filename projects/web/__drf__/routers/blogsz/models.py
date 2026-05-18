from django.db import models

# Create your models here.
class students(models.Model):
    name = models.CharField(null=True)
    age = models.IntegerField(default=18)

    def __str__(self):
        return self.name