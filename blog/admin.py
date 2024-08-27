from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "created_at", "publish", "status"]
    list_display_links = ["title", "author"]
    list_filter = ["status", "created_at", "publish", "author"]
    search_fields = ["title", "content"]
    raw_id_fields = ["author"]
    ordering = ["status", "publish"]
    date_hierarchy = "publish"
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["email", "created_at", "publish", "status"]
    list_display_links = ["publish", "email"]
    list_filter = ["status", "created_at", "publish", "email"]
    search_fields = ["email", "content"]
    ordering = ["status", "publish"]
    date_hierarchy = "publish"
