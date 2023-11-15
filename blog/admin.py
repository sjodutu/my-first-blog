from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_filter = ['published_date', 'created_date']
admin.site.register(Post)