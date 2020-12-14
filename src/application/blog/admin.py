from django.contrib import admin

from application.blog.models import BlogPost


@admin.register(BlogPost)
class PostAdminModel(admin.ModelAdmin):
    pass
