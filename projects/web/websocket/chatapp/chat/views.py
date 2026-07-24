from .models import *
from .serializers import UserSerializer , CommunicationSerializer,MessageSerializer
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view , permission_classes
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token 

@api_view(['POST'])
def Register(request):
    print(request.data)
    serializers = UserSerializer(data=request.data)
    if serializers.is_valid():
        user = User.objects.create_user(
            username=request.data['username'],
            email=request.data['email'],
            password=request.data['password']
        )           
        token = Token.objects.create(user=user)
        return Response({
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email
            },
            "token": token.key
        }, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login(request):
    username=request.data.get('username')
    password=request.data.get('password')
    user = authenticate(username=username,password=password)

    if user is not None:
        token, created = Token.objects.get_or_create(user=user)

        return Response({
                    "message": "Login Successful",
                    "token": token.key,
                    "username": user.username,
                    "user_id": user.id
                })

    return Response(
        {"errors": "Invalid User"},
        status=status.HTTP_400_BAD_REQUEST
    )

@permission_classes([IsAuthenticated])
@api_view(['GET'])
def chats(request):
    chats = Communication.objects.filter(members=request.user)
    serializers = CommunicationSerializer(chats,many=True)
    return Response(serializers.data)


@permission_classes([IsAuthenticated])
@api_view(['GET'])
def contacts(request):
    contacts = User.objects.exclude(id=request.user.id)
    serializers = UserSerializer(contacts,many=True)
    return Response(serializers.data)



@permission_classes([IsAuthenticated])
@api_view(['GET'])
def contact_chat(request,pk):
    chat=Message.objects.filter(conversation_id=pk).order_by('created_at')
    serializers = MessageSerializer(chat,many=True)
    return Response(serializers.data)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def start_chat(request):

    user_id = request.data.get("user_id")

    other_user = User.objects.get(id=user_id)

    chat = Communication.objects.filter(
        members=request.user
    ).filter(
        members=other_user
    ).first()

    if not chat:

        chat = Communication.objects.create()

        chat.members.add(request.user)
        chat.members.add(other_user)

    return Response({
        "conversation_id": chat.id
    })