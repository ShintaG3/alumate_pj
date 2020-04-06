from django.contrib import admin
from .models import Post, Query, PostComment
# Register your models here.

admin.site.register(Post)
admin.site.register(Query)
admin.site.register(PostComment)