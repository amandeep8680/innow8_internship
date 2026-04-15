from rest_framework import serializers
from .models import Book
# from . import models

class Bookinfo(serializers.ModelSerializer):
    class Meta:
        model = Book
        # model = models.Book
        fields = '__all__'
