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
        posts=Post.objects.all().order_by('-created_at')
        serializer = PostSerializer(posts , many=True)
        return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_post(request,id):
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        return Response({"error":"No Post Found"} , status = 404)
    if post.user != request.user:
         return Response({"error":"Not Allowed"},status=403)
    
    post.delete()
    return Response({"message":"Post Deleted! "})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def like_count(request ,pk):
    try:
        post=Post.objects.get(id=pk)
    except Post.DoesNotExist:
        return Response({"error":"Post Not Found"})
          
    count = post.likes.count()
    return Response({"post_id":post.id,
                    "likes_count":count})
     




@api_view(['POST','DELETE'])
@permission_classes([IsAuthenticated])
def like_unlike(request,pk):
    try:
        post = Post.objects.get(id=pk)
    except Post.DoesNotExist:
        return Response({"error":"Post Not found"})
    
    #like
    if request.method == 'POST':
        like , created = Like.objects.get_or_create(
            user=request.user,
            post=post
            )
        if not created:
            return Response({"message":"Already liked"})
        return Response({"message":"Post liked"})
       
       #unlike
    elif request.method == 'DELETE':
        deleted, _ = Like.objects.filter(
          user=request.user,
          post=post
         ).delete()
        
        if deleted == 0:
              return Response({"message":"You have not liked the post"})
        return Response({"message":"Post unliked"})









@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def comment(request,pk):
    try:
        post = Post.objects.get(id=pk)
    except Post.DoesNotExist:
        return Response({"error":"Post Not found"},status = 404)
    


    if request.method == 'GET':
        comments = post.comments.all()
        serializer = CommentSerializer(comments , many=True)
        return Response(serializer.data)
    

    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
              serializer.save(user=request.user ,post=post)
              return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

    
