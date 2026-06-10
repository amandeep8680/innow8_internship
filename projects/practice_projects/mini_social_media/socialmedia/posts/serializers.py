from rest_framework import serializers
from .models import Post , Like , Comment


class PostSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id','user','image','caption','created_at','likes_count']

    def get_likes_count(self , obj):
        return obj.likes.count()

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id','user','post']

        
class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    post = serializers.ReadOnlyField(source='post.id')  # 👈 ADD THIS

    class Meta:
        model = Comment
        fields = ['id','user','post','text','created_at']
        