stateless , usedeverywhere


## settings
rest_framewoork.authtoken

## settings 
REST_FRAMEWORK = {

    'DEFAULT_AUTHENTICATION_CLASSES': [

        'rest_framework.authentication.TokenAuthentication',
    ]
}





## views 
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class LoginView(APIView):
    def post(self,request):
        username = request.data.get('username')
        password = request.data.get('password')

        print("USERMAME : ",  username)
        print("Password :",password )

        user = authenticate(username=username , password=password)

        if user is not None:
            print("user verified")

            token , created = Token.objects.get_or_create(user=user)

            print("Token:",  token.key)

            return Response({
                'token':token.key,
                'message':'Login Successful'
            })
        
        return Response({
            'error':'Invalid credentials'
        })
    




class ProfileView(APIView):
    premission_Classes = [IsAuthenticated]

    def get(self,request):
        print("Authenticated User = ",request.user)

        return Response({
            'id':request.user.id,
            'username':request.user.username,

        })