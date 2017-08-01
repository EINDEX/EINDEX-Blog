from django.contrib import admin

# Register your models here.
from blog.models import Post, Tag


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_publish', 'created_time', 'modified_time', 'author']


admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
