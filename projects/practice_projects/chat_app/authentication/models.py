from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    '''this is a user model with all default fields and ,
    extrafields are mobile number , last_Seen ,  is_active or not '''

    mobile=models.IntegerField(null=True)
    last_seen=models.DateTimeField(null=True, blank=True)
    is_online=models.BooleanField(default=False)
