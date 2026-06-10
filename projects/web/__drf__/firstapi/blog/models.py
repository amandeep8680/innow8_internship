from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=25)
    author = models.CharField(max_length=25)
    # Add null=True and blank=True so it doesn't complain about existing data
    publishing_year = models.DateField(auto_now_add=True, null=True, blank=True) 

    def __str__(self):
        return self.title
