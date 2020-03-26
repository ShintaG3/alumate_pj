from django.db import models
from django.contrib.auth.models import User
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import date
# Create your models here.


current_year = date.today().year

gender_choices = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('NB', 'Genderqueer/Non-Binary'),
    ('NA', 'Prefer not to disclose')
]

class BaseInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    gender = models.CharField(max_length=30, choices=gender_choices, default='NA')
    birthday = models.DateField(null=True)

    def __str__(self):
        return self.user.username


current_status = [
    ('FU', 'Future Student'), ('CU', 'Current Student'), ('AL', 'Alumni')
]

class UserProfile(models.Model):
    # Many field are optional as a User may be a student 
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=20, default='anonymous')
    status = models.CharField(max_length=20, choices=current_status, default='CU')
    country_origin = models.CharField(max_length=50, null=True, blank=True)
    country_study_abroad = models.CharField(max_length=50, null=True, blank=True)
    school = models.CharField(max_length=50, null=True, blank=True)
    major = models.CharField(max_length=50, null=True, blank=True)
    school_start_year = models.IntegerField(
        validators = [MaxValueValidator(current_year+2), MinValueValidator(1940)],
        null=True, blank=True
    )
    school_end_year = models.IntegerField(
        validators = [MaxValueValidator(current_year+10), MinValueValidator(1940)],
        null=True, blank=True
    )
    living_city = models.ForeignKey('City', on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.user.username


class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    goal = models.CharField(max_length=30)

    def __str__(self):
        return self.user.username + "'s goal: " + self.goal

class StudyInterest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    field = models.CharField(max_length=30)
    
    def __str__(self):
        return self.user.username + "'s study interest: " + self.goal
    

class WorkExperience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=30) 
    position = models.CharField(max_length=30)
    start_year = models.IntegerField(
        validators = [MaxValueValidator(current_year), MinValueValidator(1970)]
    )
    end_year = models.IntegerField(
        validators = [MaxValueValidator(current_year), MinValueValidator(1970)],
        null=True, blank=True
    )
    is_present = models.BooleanField()
    
    def __str__(self):
        return self.name + ' worked at ' + self.company + ' as ' + self.position 
    

social_link_type = [
    ('FB', 'Facebook'), ('TW', 'Twitter'), ('LN', 'LinkedIn'), ('IG', 'Instagram'),
    ('BL', 'Blog')
]

class SocialLink(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    link_type = models.CharField(max_length=20, choices=social_link_type)
    url = models.URLField()

    def __str__(self):
        return 
    
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
        return self.city_name + ', ' + self.country.country_name

class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    followed = models.ForeignKey(User, related_name='followed_user', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.follower.username + ' following ' + self.followed.username

# class Message(models.Model):
#     sender = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, related_name='message_sender')
#     reciever = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, related_name='message_reciever')
#     message = models.CharField(max_length=500)
#     timestamp = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.message

