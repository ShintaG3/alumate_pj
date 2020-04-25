from django import forms
from django.db import models
from django.contrib.auth.models import User
from accounts.models import School, Country, Major, BasicInfo, City
from django.db.models.signals import pre_save
from alumate.utils import unique_slug_generator, unique_slug_generator_post
from django.urls import reverse

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.CharField(max_length=5000)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ('-created_at',)
    
    def __str__(self):
        return self.user.username + "'s post: " + self.body[:10] + "..."
    
    def get_absolute_url(self):
        return reverse("post_detail", args=[str(self.id)])
    
class PostComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    body = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    likes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('created_at',)
    
    def __str__(self):
        return self.user.username + "'s comment on: " + self.post + ": " + self.body[:10] + "..."

class PostLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_likes")


class PostCommentLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(PostComment, on_delete=models.CASCADE, related_name="comment_likes")

