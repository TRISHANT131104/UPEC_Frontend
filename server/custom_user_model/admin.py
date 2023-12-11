from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class CustomUserAdmin(UserAdmin):
    list_display = (
        "id",
        "username",
        "email",
        "first_name",
        "last_name",
        "is_staff",
        "is_active",
        "last_login",
        "role",
        "image"
    )

User = get_user_model()
admin.site.register(User, CustomUserAdmin)