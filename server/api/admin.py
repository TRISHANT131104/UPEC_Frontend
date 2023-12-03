from django.contrib import admin
from .models import Post, ChatMsg, GroupMessage, Group
from django.contrib.auth import get_user_model
 # import UserAdmin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
User = get_user_model()
class CustomUserAdmin(UserAdmin):
    list_display = ('id','username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'last_login')

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

admin.site.register(Post)

admin.site.register(ChatMsg)

admin.site.register(GroupMessage)

admin.site.register(Group)