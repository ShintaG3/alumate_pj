from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Post)
admin.site.register(PostComment)
admin.site.register(Ask)
admin.site.register(AskTagStatus)
admin.site.register(AskTagHomeCountry)
admin.site.register(AskTagStudyAbroadCountry)
admin.site.register(AskTagSchool)
admin.site.register(AskTagMajor)
admin.site.register(AskTagStartYear)
admin.site.register(AskTagEndYear)
