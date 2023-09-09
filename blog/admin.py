from django.contrib import admin
from .models import Post, Comment


class CommentInLine(admin.TabularInline):
    model = Comment
    extra = 0


class PostAdmin(admin.ModelAdmin):
    inlines = [CommentInLine]


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
# Register your models here.
