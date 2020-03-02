from django.db import models
from django.contrib.auth.models import User
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

current_status = (
    ('future', 'future'),
    ('student', 'student'),
    ('alumni', 'alumni')
)

class BaseInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=20, choices= current_status)
    school = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    year_of_abroad_study = models.CharField(max_length=15)
    job_before_abroad_study = models.CharField(max_length=100)
    job_after_abroad_study = models.CharField(max_length=100)
 
class UserProfile(models.Model):
    # Many field are optional as a User may be a student 
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    about = models.CharField(max_length=200)
    school_start_year = models.IntegerField(
        validators = [MaxValueValidator(2020), MinValueValidator(1940)],
        null=True, blank=True
        )
    school_end_year = models.IntegerField(
        validators = [MaxValueValidator(2020), MinValueValidator(1940)],
        null=True, blank=True
        )
    previous_job = models.CharField(max_length=100, null=True, blank=True)
    previous_job_start_year = models.IntegerField(
        validators = [MaxValueValidator(2020), MinValueValidator(1970)],
        null=True, blank=True
        )
    previous_job_end_year = models.IntegerField(
        validators = [MaxValueValidator(2020), MinValueValidator(1970)],
        null=True, blank=True
        )
    post_job = models.CharField(max_length=100, null=True, blank=True)
    living_country = models.ForeignKey('Country', on_delete=models.SET_NULL, null=True)
    living_city = models.ForeignKey('City', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField()
    follower = models.IntegerField(default=0)
    following = models.IntegerField(default=0)
    posts = models.IntegerField(default=0)
    slug = models.SlugField(max_length=40)
    last_message_read_time = models.DateTimeField()

    def get_new_messages(self):
        last_read_time = self.last_message_read_time or datetime(1900, 1, 1)
        return Message.objects.filter(sender=self).filter(
            Message.timestamp > self.last_message_read_time
        ).count()

    def __str__(self):
        return self.user.username
    
class School(models.Model):
    school_name = models.CharField(max_length=50)
    country = models.ForeignKey('Country', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.school_name

class Country(models.Model):
    country_name = models.CharField(max_length=50)   # change in to choose filed
    
    def __str__(self):
        return self.country_name

class City(models.Model):
    city_name = models.CharField(max_length=50)
    country = models.ForeignKey('Country', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.city_name

class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    followed = models.ForeignKey(User, related_name='followed_user', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.follower.username

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='message_sender')
    reciever = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='message_reciever')
    timestamp = models.DateTimeField(auto_now_add=True)


