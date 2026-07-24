from django.contrib.auth import authenticate, login,get_user_model
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

User = get_user_model()
class UserAuthViewSet(viewsets.ViewSet):


    def register(self , request):
        username = request.data.get("username")
        password = request.data.get("password")
    
        User.objects.create_user(
            username = username,
            password = password
        )
        return Response({"message":"User Registered"})

    
    @action(detail=False, methods=["post"])
    def login(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is None:
            return Response(
                {"error": "Invalid username or password"},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        login(request, user)

        return Response(
            {
                "message": "Login successful",
                "user_id": user.id,
            },
            status=status.HTTP_200_OK,
        )