from django.contrib import admin
from .models import UserProfile, School, Country, City, Follow
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(School)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Follow)