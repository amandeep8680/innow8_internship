from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import serializers
from .models import User
from .exception import InvalidCredentials , UserAlreadyExists
from django.contrib.auth import authenticate 

class RegisterService:
    @staticmethod   
    def register(data):
        username=data["username"]
        password=data["password"] 
        
        if User.objects.filter(username=username).exists():
                raise UserAlreadyExists()
            
        User.objects.create_user(
            username=username,
            password=password,
        )
        return {
        "message":"User Registered"
    }







class AuthService:
    @staticmethod
    def login(data):
        username=data["username"]
        password=data["password"]


        user = authenticate(
            username=username,
            password = password
        )

        if not user:
            raise InvalidCredentials()

        refresh = RefreshToken.for_user(user)

        return{
            "access":str(refresh.access_token),
            "refresh":str(refresh),
        }