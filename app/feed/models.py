from django import forms
from django.db import models
from django.contrib.auth.models import User
from accounts.models import School, Country, Major, BasicInfo, City
from django.db.models.signals import pre_save
from alumate.utils import unique_slug_generator, unique_slug_generator_post
from django.urls import reverse
from accounts.models import CurrentStatus

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

class Ask(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=3000)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.__str__() + ": " + self.title

    class Meta:
        ordering = ['created_at']

class AskTag(models.Model):
    ask = models.ForeignKey(Ask, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        abstract = True

class AskTagStatus(AskTag):
    body = models.CharField(max_length=20, choices=CurrentStatus.choices, default=CurrentStatus.CURRENT_STUDENT)

class AskTagHomeCountry(AskTag):
    body = models.ForeignKey(Country, on_delete=models.SET_NULL, related_name="ask_country_origin", null=True, blank=True)

class AskTagStudyAbroadCountry(AskTag):
    body = models.ForeignKey(Country, on_delete=models.SET_NULL, related_name="ask_country_study_abroad", null=True, blank=True)

class AskTagSchool(AskTag):
    body = models.ForeignKey(School, on_delete=models.CASCADE, related_name='ask_school')

class AskTagMajor(AskTag):
    body =  models.ForeignKey(Major, on_delete=models.CASCADE, related_name='ask_school')

class AskTagStartYear(AskTag):
    lower_bound =  models.IntegerField(null=True, blank=True)
    upper_bound =  models.IntegerField(null=True, blank=True)

class AskTagEndYear(AskTag):
    lower_bound = models.IntegerField(null=True, blank=True)
    upper_bound = models.IntegerField(null=True, blank=True)

# class AskTagHomeCountry(models.Model):
#     living_city = models.ForeignKey('City', on_delete=models.SET_NULL, null=True, blank=True)