from django.db import models
from django.contrib.auth.models import User
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

current_status = (
    ('preparing', 'preparing'),
    ('student', 'student'),
    ('alumni', 'alumni')
)

class UserProfile(models.Model):
    # Many field are optional as a User may be a student 
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    about = models.CharField(max_length=200)
    school = models.ManyToManyField('School')
    school_start_year = models.IntegerField(
        validators = [MaxValueValidator(2020), MinValueValidator(1940)],
        null=True, blank=True
        )
    school_end_year = models.IntegerField(
        validators = [MaxValueValidator(2020), MinValueValidator(1940)],
        null=True, blank=True
        )
    # Should a User must have a course ?
    course = models.CharField(max_length=50, null=True, blank=True)
    previus_job = models.CharField(max_length=100, null=True, blank=True)
    previus_job_start_year = models.IntegerField(
        validators = [MaxValueValidator(2020), MinValueValidator(1970)],
        null=True, blank=True
        )
    previus_job_end_year = models.IntegerField(
        validators = [MaxValueValidator(2020), MinValueValidator(1970)],
        null=True, blank=True
        )
    living_country = models.ForeignKey('Country', on_delete=models.SET_NULL, null=True)
    living_city = models.ForeignKey('City', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField()
    status = models.CharField(max_length=20, choices= current_status)
    follower = models.IntegerField(default=0)
    following = models.IntegerField(default=0)
    posts = models.IntegerField(default=0)
        
    def __str__(self):
        return self.about
    
class School(models.Model):
    school_name = models.CharField(max_length=50)
    country = models.ForeignKey('Country',on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.school_name

class Country(models.Model):
    country_name = models.CharField(max_length=50)

    def __str__(self):
        return self.country_name

class City(models.Model):
    city_name = models.CharField(max_length=50)
    country = models.ForeignKey('Country', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.city_name

