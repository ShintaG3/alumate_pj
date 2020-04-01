from django.contrib import admin
from .models import Profile, School, Country, City, Follow, BasicInfo, StudyInterest, Goal
# Register your models here.
admin.site.register(Profile)
admin.site.register(School)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Follow)
admin.site.register(BasicInfo)
admin.site.register(Goal)
admin.site.register(StudyInterest)
