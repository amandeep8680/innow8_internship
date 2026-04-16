from django.contrib.auth.models import User
from .models import Profile
from .serializers import UserSerializer  , ProfileSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view , permission_classes
from rest_framework import status
from django.contrib.auth import authenticate , login , logout
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

@api_view(['POST'])
def Register(request):
    if request.method == "POST":
        serializers = UserSerializer(data=request.data)
        if serializers.is_valid():
            user = serializers.save()

            Profile.objects.create(user=user)

            token = Token.objects.create(user=user)

            return Response({
                "user":serializers.data,
                "token":token.key
                }, status=status.HTTP_201_CREATED)
        
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['POST'])
def User_login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username,password=password)

    if user is not None:
        token, _ = Token.objects.get_or_create(user=user)

        return Response({"message":"Login Successful",
                         "token":token.key})
    
    return Response({"errors":"Invalid User"},status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET','PUT'])
@permission_classes([IsAuthenticated])
def profile_view(request):
    user = request.user
    profile = Profile.objects.get(user=user)

    if request.method == 'GET':
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    elif request.method =='PUT':
        serializer = ProfileSerializer(profile , data=request.data ,  partial = True )
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response(serializer.data)
        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)
