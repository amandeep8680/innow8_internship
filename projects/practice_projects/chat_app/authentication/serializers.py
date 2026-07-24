from rest_framework import serializers
from .models import User

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        models=User
        fields = "__all__"


class RegisterLoginSerializer(serializers.Serializer):
     username = serializers.CharField(max_length=20)
     password = serializers.CharField(write_only=True , min_length = 2)



