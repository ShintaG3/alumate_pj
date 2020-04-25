from django.db import models
from django.contrib.auth.models import User
from accounts.models import CurrentStatus
from accounts.models import Country, School, Major

# Create your models here.

class Ask(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=3000)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.__str__() + ": " + self.title

    class Meta:
        ordering = ['-created_at']

class AskComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ask = models.ForeignKey(Ask, on_delete=models.CASCADE, related_name="comments")
    body = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

class AskLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ask = models.ForeignKey(Ask, on_delete=models.CASCADE, related_name="likes")

class AskCommentLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(AskComment, on_delete=models.CASCADE, related_name="likes")

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

# class AskTagHomeCountry(models.Model):
#     living_city = models.ForeignKey('City', on_delete=models.SET_NULL, null=True, blank=True)

class AskTagStartYear(AskTag):
    lower_bound =  models.IntegerField(null=True, blank=True)
    upper_bound =  models.IntegerField(null=True, blank=True)

class AskTagEndYear(AskTag):
    lower_bound = models.IntegerField(null=True, blank=True)
    upper_bound = models.IntegerField(null=True, blank=True)
