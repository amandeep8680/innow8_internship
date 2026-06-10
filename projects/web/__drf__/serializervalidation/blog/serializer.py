from rest_framework import serializers
from django.db import models## Firld level serializer
# method name :
# validate_<fieldname>
class User_serializer(serializers.Serializer):
    username = serializers.CharField()

    def validate_username(self , value):
        if "admin" in value.lower():
            raise serializers.ValidationError("Username can't be 'admin'")
        return value
    
    def create(self , validate_data):
        return self.username.objects.create(**validate_data)


        



# Object Level Validation
# ✔ Runs after all field-level validations
# method  ; def validate(self , datA)
class RegisterSerializer(serializers.Serializer):
    password = serializers.CharField()
    confirm_Password = serializers.CharField()

    def validate(self , data):
        if data['password'] != data['confirm_passwprd']:
            raise serializers.ValidationError("Password do no match")








# using validator  :
# reusable and clean
def validate_even(value):
    if value % 2 !=  0:
        raise serializers.ValidationError("Only even number are allowed")
 

# class NumberSerializer(serializers.Serializer):
#     number = serializers.IntegerField(validator = [validate_even])









# model serializer:
# from .models import Profile

# class ProfileSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = Profile
#         fields = '__all__'

#     def validate_age(self, value):
#         if value < 18:
#             raise serializers.ValidationError("Age must be 18+")
#         return value