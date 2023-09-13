from django.contrib import admin
from .models import Post,Comment

@admin.register(Post)
class MyModelAdmin(admin.ModelAdmin):
    fields = ('author', 'name','school','images','studyday_type','comment','published_date')
    list_display = ('author', 'name','school','images','studyday_type','comment','published_date')

@admin.register(Comment)
class MyModelAdmin(admin.ModelAdmin):
    fields = ('content',)
    list_display = ('content',)

