from rest_framework import serializers
from . import models

class aboutprofile(serializers.ModelSerializer):
    class Meta:
        model = models.profiles
        fields = '__all__'