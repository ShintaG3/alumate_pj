from django.db import models
from django.contrib.auth.models import User
from accounts.models import School, Country, UserProfile, City
from django.db.models.signals import pre_save
from alumate.utils import unique_slug_generator, unique_slug_generator_post

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    body = models.CharField(max_length=5000)
    post_created_at = models.DateTimeField(auto_now_add=True)
    post_edited_at = models.DateTimeField(blank=True, null=True)
    post_likes = models.IntegerField(default=0)
    post_views = models.IntegerField(default=0)
    post_replies = models.IntegerField(default=0)
    slug = models.SlugField(max_length=40, null=True, blank=True)

    def __str__(self):
        return self.body

class Query(models.Model):
    query_creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    query_title = models.CharField(max_length=100)  
    query_body = models.CharField(max_length=1000)
    query_created_at = models.DateTimeField()
    query_school_tag = models.ManyToManyField(School, blank=True)
    query_country_tag = models.ManyToManyField(Country, blank=True)
    query_city_tag = models.ManyToManyField(City, blank=True)
    query_resolved = models.BooleanField()
    query_resolved_by = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='resolved_by')
    slug = models.SlugField(max_length=40, null=True, blank=True)

    def __str__(self):
        return self.query_title

def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

def slug_generator_post(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator_post(instance)

pre_save.connect(slug_generator, sender=Query)
pre_save.connect(slug_generator_post, sender=Post)
    

