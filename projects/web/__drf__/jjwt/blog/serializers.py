from rest_framework import serializers
from django.contrib.auth.models import User 

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =['username','password','email']

        extra_kwargs = {
            'password':{'write_only':True}
        }

    def create(self , validate_data):
        user = User.objects.create_user(
            username = validate_data['username'],
            email = validate_data['email'],
            password=validate_data['password']
        )
        return user


        