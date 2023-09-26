from django.contrib import admin
from .models import Post,Comment

@admin.register(Post)
class MyModelAdmin(admin.ModelAdmin):
    fields = ('author', 'name','katakana','school','images','studyday_type','published_date')
    list_display = ('author', 'name','katakana','school','images','studyday_type','published_date')
