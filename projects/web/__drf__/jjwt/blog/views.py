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

