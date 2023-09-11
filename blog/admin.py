from django.contrib import admin
from .models import Post

@admin.register(Post)
class MyModelAdmin(admin.ModelAdmin):
    fields = ('author', 'name','school','images','studyday_type', 'text','published_date')
    list_display = ('author', 'name','school','images','studyday_type', 'text','published_date')