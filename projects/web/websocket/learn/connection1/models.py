from django.db import models

# Create your models here.
class Message(models.Model):
    sender = models.CharField(max_length=30)
    receiver = models.CharField(max_length=30)
    message = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.message
    
