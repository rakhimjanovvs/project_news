from django.contrib import admin
from .models import News, NewsCategory, Comment

# Register your models here.
admin.site.register(News)
admin.site.register(NewsCategory)
admin.site.register(Comment)