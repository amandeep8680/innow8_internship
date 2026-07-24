from .serializers import CreateRoomSerializer
from .services import GroupChatServices , ChatServices
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .response import success_response


    
class CreateRoomView(APIView):

    permission_classes = [
        IsAuthenticated
    ]


    def post(self, request):

        serializer = CreateRoomSerializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )


        room_id = GroupChatServices.create_room(
            request.user,
            serializer.validated_data["name"],
            serializer.validated_data["members"]
        )
        return success_response(
            {
                "room_id": room_id
            },
            message="Room created successfully"
    
        )