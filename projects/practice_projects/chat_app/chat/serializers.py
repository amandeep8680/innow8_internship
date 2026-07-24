from rest_framework import serializers
from .models import OneToOneChat ,ChatRoom

class OneToOneChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = OneToOneChat
        fields = "__all__"




## groupcreationserializer


class CreateRoomSerializer(serializers.Serializer):

    name = serializers.CharField(
        max_length=100
    )

    members = serializers.ListField(
        child=serializers.IntegerField(),
        allow_empty = False
    )
    
    def validate_members(self, value):

        if len(value) != len(set(value)):
            raise serializers.ValidationError(
                "Duplicate members not allowed"
            )

        return value