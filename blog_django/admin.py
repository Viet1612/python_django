from django.contrib import admin
from .models import User
from .models import Post
from .models import Comment
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_name', 'email', 'passw', 'image']
    list_filter = ['user_name']
    search_fields = ['user_name']
    
admin.site.register(User, UserAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'title', 'contend', 'date']
    list_filter = ['user']
    search_fields = ['user']
    
admin.site.register(Post, PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'post', 'comment', 'date']
    list_filter = ['user']
    search_fields = ['user']
    
admin.site.register(Comment, CommentAdmin)