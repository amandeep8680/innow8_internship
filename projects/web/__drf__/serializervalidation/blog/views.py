from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import User_serializer

@api_view(['POST'])
def create(request):
    serializer = User_serializer(data=request.data)
    
    if serializer.is_valid():
        return Response(serializer.validated_data)
    
    return Response(serializer.errors, status=400)


@api_view(['GET'])
def show(request):
    queryset = username.objects.all() 
    serializer =  User_serializer(queryset , many=True)
    return Response(serializer.data)