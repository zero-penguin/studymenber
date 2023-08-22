from django.contrib import admin
from .models import Post

@admin.register(Post)
class MyModelAdmin(admin.ModelAdmin):
    fields = ('author', 'title', 'text','created_date','published_date')
    list_display = ('author', 'title', 'text','created_date','published_date')