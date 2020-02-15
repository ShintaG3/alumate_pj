from django.contrib import admin
from .models import UserProfile, School, City, Country
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(School)
admin.site.register(City)
admin.site.register(Country)
