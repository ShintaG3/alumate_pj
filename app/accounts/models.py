from django.db import models
from django.contrib.auth.models import User
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import date
from django.utils.translation import gettext_lazy as _
# Create your models here.


current_year = date.today().year

class Gender(models.TextChoices):
    MALE = 'M', _('Male'),
    FEMALE = 'F', _('Female'),
    NON_BINARY = 'NB', _('Genderqueer/Non-Binary'),
    NO_ANSWER = 'NA', _('Prefer not to disclose')
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    gender = models.CharField(max_length=30, choices=Gender.choices, default=Gender.NO_ANSWER)
    birthday = models.IntegerField(null=True)

    def __str__(self):
        return self.user.username

class CurrentStatus(models.TextChoices):
    FUTURE_STUDENT = 'FU', _('Future Student'),
    CURRENT_STUDENT = 'CU', _('Current Student'),
    ALUMNI = 'AL', _('Alumni')

class BasicInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=40)
    status = models.CharField(max_length=20, choices=CurrentStatus.choices, default=CurrentStatus.CURRENT_STUDENT)
    country_origin = models.CharField(max_length=50, null=True, blank=True)
    country_study_abroad = models.CharField(max_length=50, null=True, blank=True)
    # living_city = models.ForeignKey('City', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.user.username
    
class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.CharField(max_length=30)

    def __str__(self):
        return self.user.username + "'s goal: " + self.body

class StudyInterest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.CharField(max_length=30)
    
    def __str__(self):
        return self.user.username + "'s study interest: " + self.body


class About(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.CharField(max_length=500, null=True, blank=True)
    
    def __str__(self):
        return self.user.username + "'s about: " + self.body

class EducationStatus(models.TextChoices):
    CURRENT = 'C', _('I am currently studying at this school'),
    PAST = 'P', _('I studied at this school'),
    FUTURE = 'F', _('I am going to study at this school'),
    TARGET = 'T', _('This is my target school'),
    

class History(models.Model):
    start_year =  models.CharField(max_length=20, null=True, blank=True)
    end_year = models.CharField(max_length=20, null=True, blank=True)
    
    class Meta:
        abstract = True
        ordering= ['-end_year', '-start_year']
    
class Education(History):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    school = models.CharField(max_length=50)
    major = models.CharField(max_length=50)
    # status = models.CharField(max_length=30, choices=EducationStatus.choices, default=EducationStatus.CURRENT)
    
    def __str__(self):
        return self.user.username + "'s education at " + self.school


class WorkStatus(models.TextChoices):
    PAST = 'P', _('I worked at this company'),
    CURRENT = 'C', _('I am currently working at this company'),
    TARGET = 'T', _('This is my target company'),

class WorkExperience(History):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=30) 
    position = models.CharField(max_length=30)
    # status = models.CharField(max_length=30, choices=WorkStatus.choices, default=WorkStatus.PAST)
    
    def __str__(self):
        return self.user.username + ' worked at ' + self.company + ' as ' + self.position 
    
class Scholarship(History):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    organization = models.CharField(max_length=100)
    title = models.CharField(max_length=100)


class SocialLink(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
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
    follower = models.ForeignKey(User, on_delete=models.CASCADE)
    followed = models.ForeignKey(User, related_name='followed_user', on_delete=models.CASCADE)

    def __str__(self):
        return self.follower.username + ' following ' + self.followed.username

# class Message(models.Model):
#     sender = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, related_name='message_sender')
#     reciever = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, related_name='message_reciever')
#     message = models.CharField(max_length=500)
#     timestamp = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.message

