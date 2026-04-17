from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE , related_name='posts')
    image = models.ImageField(upload_to='posts/')
    caption = models.TextField(blank=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - Post {self.id}"
    


class Like(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    post = models.ForeignKey(Post , on_delete=models.CASCADE , related_name='likes' )

    def __str__(self):
        return f"{self.user.username} like Post {self.post.id}"
    
    class Meta:
        unique_together = ['user','post']



class Comment(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    post = models.ForeignKey(Post , on_delete=models.CASCADE , related_name='comments')
    text = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} commented on post {self.post.id}"