from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user  = models.OneToOneField(User , on_delete=models.CASCADE)
    dob = models.DateField(null = True , blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics/',null=True, blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username
    