from rest_framework import viewsets 
from rest_framework.decorators import action
from .services import AuthService ,RegisterService
from .responses import success_response 
from .serializers import RegisterLoginSerializer
from chat.services import  ChatServices
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated



# Create your views here.

# for user registration , login ,  logout  
class UserAuthViewSet(viewsets.ViewSet):
    @action(detail=False, methods=["post"])

    def register(self,request):
        serializer = RegisterLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data=RegisterService.register(serializer.validated_data)
        return success_response(data)
    





    def login(self,request):
        serializer = RegisterLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = AuthService.login(serializer.validated_data)
        return success_response(data)




class ChatGroupView(APIView):

    permission_classes = [
        IsAuthenticated
    ]


    def get(self, request):

        all_users = ChatServices.get_users(request)

        groups = ChatServices.get_group(request)


        return success_response({
            "users": all_users,
            "groups": groups
        },message="contacts Fetched ")
