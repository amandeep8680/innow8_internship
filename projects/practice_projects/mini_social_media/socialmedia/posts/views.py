from .models import Post , Like , Comment
from .serializers import PostSerializer , CommentSerializer , LikeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import IsAuthenticated


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_post(request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.error , status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_posts(request):
        posts=Post.objects.all().order_by('-createdd_At')
        serializer = PostSerializer(posts , many=True)
        return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_post(request,id):
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        return Response({"errors":"No Post Found"} , status = 404)
    if post.user != request.user:
         return Response({"error":"Not Allowed"},status=403)
    
    post.delete()
    return Response({"message":"Post Deleted! "})







