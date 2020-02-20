from django.db import models
from django.contrib.auth.models import User
from user_profile.models import School, Country, UserProfile, City
    
class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    post_title = models.CharField(max_length=100)
    body = models.CharField(max_length=5000)
    post_country_tag = models.ManyToManyField(Country)
    post_city_tag = models.ManyToManyField(City)
    post_school_tag = models.ManyToManyField(School)
    #Should'nt the post be displayed in paragraphs instead of one big body ?
    # p1 = models.CharField(max_length=500)
    # p2 = models.CharField(max_length=500, blank=True)
    # p3 = models.CharField(max_length=500, blank=True)
    # p4 = models.CharField(max_length=500, blank=True)
    post_created_at = models.DateTimeField(auto_now_add=True)
    post_edited_at = models.DateTimeField(blank=True)
    post_likes = models.IntegerField(default=0)
    post_views = models.IntegerField(default=0)
    post_replies = models.IntegerField(default=0)
    slug = models.CharField(max_length=100)

    def __str__(self):
        return self.post_title

class Query(models.Model):
    query_creator = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True)
    query_title = models.CharField(max_length=100)
    query_body = models.CharField(max_length=1000)
    query_created_at = models.DateTimeField()
    query_resolved = models.BooleanField()
    #query_resolved_by = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.query_title
    

