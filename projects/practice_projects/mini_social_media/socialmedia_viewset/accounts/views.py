from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User
from .models import Profile
from .serializers import UserSerializer, ProfileSerializer


class AuthViewSet(viewsets.ViewSet):

    # ✅ REGISTER
    @action(detail=False, methods=['post'])
    def register(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()

            Profile.objects.create(user=user)
            token = Token.objects.create(user=user)

            return Response({
                "user": serializer.data,
                "token": token.key
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # ✅ LOGIN
    @action(detail=False, methods=['post'])
    def login(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user:
            token, _ = Token.objects.get_or_create(user=user)

            return Response({
                "message": "Login Successful",
                "token": token.key
            })

        return Response({"error": "Invalid credentials"}, status=400)


class ProfileViewSet(viewsets.ViewSet):

    permission_classes = [IsAuthenticated]

    # ✅ GET PROFILE
    def list(self, request):
        profile = Profile.objects.get(user=request.user)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    # ✅ UPDATE PROFILE
    def update(self, request, pk=None):
        profile = Profile.objects.get(user=request.user)

        serializer = ProfileSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)