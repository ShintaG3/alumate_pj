from django.contrib import admin
from .models import UserProfile, School, Country, City
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(School)
admin.site.register(Country)
admin.site.register(City)