from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Post, Like, Comment
from .serializers import PostSerializer, CommentSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    # ✅ CREATE POST
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    # ✅ DELETE POST
    def destroy(self, request, *args, **kwargs):
        post = self.get_object()

        if post.user != request.user:
            return Response({"error": "Not allowed"}, status=403)

        post.delete()
        return Response({"message": "Post deleted"})

    # ✅ LIKE COUNT
    @action(detail=True, methods=['get'])
    def like_count(self, request, pk=None):
        post = self.get_object()
        return Response({
            "post_id": post.id,
            "likes_count": post.likes.count()
        })

    # ✅ LIKE / UNLIKE
    @action(detail=True, methods=['post', 'delete'])
    def like_unlike(self, request, pk=None):
        post = self.get_object()

        # LIKE
        if request.method == 'POST':
            like, created = Like.objects.get_or_create(
                user=request.user,
                post=post
            )
            if not created:
                return Response({"message": "Already liked"})
            return Response({"message": "Post liked"})

        elif request.method == 'DELETE':
            deleted, _ = Like.objects.filter(
                user=request.user,
                post=post
            ).delete()

            if deleted == 0:
                return Response({"message": "You have not liked this post"})
            return Response({"message": "Post unliked"})

    # ✅ COMMENTS (GET + POST)
    @action(detail=True, methods=['get', 'post'])
    def comment(self, request, pk=None):
        post = self.get_object()

        # GET COMMENTS
        if request.method == 'GET':
            comments = post.comments.all()
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data)

        # ADD COMMENT
        elif request.method == 'POST':
            serializer = CommentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user=request.user, post=post)
                return Response(serializer.data, status=201)

            return Response(serializer.errors, status=400)  