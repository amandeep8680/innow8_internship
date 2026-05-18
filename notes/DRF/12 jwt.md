## JWT Authentication in Django REST Framework

JWT = JSON Web Token

Used for:

Login authentication
Secure APIs
Mobile apps
React/Vue/Flutter frontend
Stateless authentication

# Most common package in DRF:

Simple JWT Documentation

Package:

djangorestframework-simplejwt


# 1. What is JWT?

JWT is a token-based authentication system.

Instead of storing session on server:

Server creates a token
Client stores token
Client sends token in every request

Example:

Authorization: Bearer eyJhbGciOiJIUzI1Ni...
# 2. Real Life Flow
Without JWT
User Login
→ Server creates session
→ Session stored in DB
→ Browser gets sessionid cookie
→ Browser sends cookie every request
With JWT
User Login
→ Server verifies credentials
→ Server creates JWT token
→ Client stores token
→ Client sends token every request
→ Server verifies token


# 3. Why JWT?
Advantages:

Stateless
Fast
Good for APIs
Mobile friendly
React/Flutter friendly
No session database lookup

Disadvantages:

Logout difficult
Token theft risk
Harder revoke system



## Add JWT Authentication
settings.py
from datetime import timedelta

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}


















from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer



# Create your views here.
class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response({
            "message":"Register Successfully"
        })
        return Response(serializer.errors)
    

class LoginView(APIView):

    def post(self,request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(
            username = username,
            password = password
        )

        if user is not None:

            refresh = RefreshToken.for_user(user)

            return Response  ({
                "refresh":str(refresh),
                "access":str(refresh.access_token)


            })
        return Response({
            "error":"Invalid Credentials"
        })
    

class ProfileView(APIView):
    permission_classes=[IsAuthenticated]

    def get(self , request):
        return Response({
            "message":"Authenticated User",
            "username":request.user.username,
            "email":"request.user.email"
        })



class LogoutView(APIView):
    permission_classes=[IsAuthenticated]

    def post(self,request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response({
                "message":"Logout Seccessful"
            })
        except Exception as e:
            return Response({
                "error":str(e)
            })

























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


        














        REST_FRAMEWORK={
    'DEFAULT_AUTHENTICATION_CLASSES':(
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),

    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": True,

    "ALGORITHM": "HS256",

    "SIGNING_KEY": SECRET_KEY,

    "AUTH_HEADER_TYPES": ("Bearer",),
}

































## SETTING

from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('blog.urls')),
    path(
        'token/refresh/',
        TokenRefreshView.as_view()
    ),
]






