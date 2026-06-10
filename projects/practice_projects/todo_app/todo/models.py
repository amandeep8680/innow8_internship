from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200, default="Untitled")  
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


def _str__(self):
    return self.title