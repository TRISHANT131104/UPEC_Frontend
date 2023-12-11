from .models.user import User
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .models import (ChatMsg, Client, Group, GroupMessage, Mentor, Milestone,
                     Post, Project, ProjectMembers, ProjectProgressReport,
                     ProjectRequirementDocument, Talent, Workflow, Team)

User = get_user_model()


class CustomUserAdmin(UserAdmin):
    """
    Custom admin class for managing User model in the Django admin site.
    """
    list_display = (
        "id",
        "username",
        "email",
        "first_name",
        "last_name",
        "is_staff",
        "is_active",
        "last_login",
    )
    list_filter = ("is_staff", "is_active")
    search_fields = ("username", "email")
    ordering = ("username",)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

admin.site.register(Post)

admin.site.register(ChatMsg)

admin.site.register(GroupMessage)

admin.site.register(Group)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """
    Custom admin class for managing Project model in the Django admin site.
    """
    list_display = ("id", "title", "created_by", "created_at")
    list_filter = ("status", "created_at", "updated_at")
    search_fields = ("title",)


admin.site.register(Milestone)

admin.site.register(ProjectProgressReport)

admin.site.register(ProjectMembers)

admin.site.register(ProjectRequirementDocument)

class CustomClientAdmin(admin.ModelAdmin):
    """
    Custom admin class for managing Client model in the Django admin site.
    """
    list_display = ["id", "user"]
    list_filter = ("user__is_active",)
    search_fields = ("user__username", "user__email")
    ordering = ("user__username",)

admin.site.register(Client, CustomClientAdmin)

admin.site.register(Mentor)


class CustomTalentAdmin(admin.ModelAdmin):
    """
    Custom admin class for managing Talent model in the Django admin site.
    """
    list_display = ["id", "user"]
    list_filter = ("user__is_active",)
    search_fields = ("user__username", "user__email")
    ordering = ("user__username",)


admin.site.register(Talent, CustomTalentAdmin)

admin.site.register(Team)

admin.site.register(Workflow)
