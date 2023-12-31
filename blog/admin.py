from django.contrib import admin
from .models import Post,Comment,Account

@admin.register(Post)
class MyModelAdmin(admin.ModelAdmin):
    fields = ('author', 'userid','name','katakana','school','school_year','images','studyday_type','published_date')
    list_display = ('author','userid','name','katakana','school','school_year','images','studyday_type','published_date')

admin.site.register(Comment)
admin.site.register(Account)
