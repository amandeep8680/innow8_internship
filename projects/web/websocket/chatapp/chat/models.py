from django.db import models # type: ignore
from django.contrib.auth.models import AbstractUser # type: ignore

class User(AbstractUser):
    phone = models.IntegerField(unique=True,null=True,blank=True)


class Communication(models.Model):
    Type_choice = (
        ('private','Private'),
        ('group','Group')
    )
    type = models.CharField(max_length=10, choices = Type_choice)
    name = models.CharField(max_length=15,null=True , blank=True)
    members = models.ManyToManyField(User) 


class Message(models.Model):
    conversation = models.ForeignKey(Communication, on_delete=models.CASCADE, related_name="messages")
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

