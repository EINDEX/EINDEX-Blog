from django.contrib import admin

# Register your models here.
from blog.models import Post, Tag


def make_published(modeladmin, request, queryset):
    queryset.update(is_publish=True)


make_published.short_description = "发布选中文章"


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_publish', 'created_time', 'modified_time', 'author']
    actions = [make_published]


admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
