import uuid
from django.contrib.auth.models import (
    AbstractBaseUser,
    AbstractUser,
    BaseUserManager,
    PermissionsMixin,
    
)
from django.db import models
from django.utils import timezone

from ..helpers import getdate, gettime
from .projects import Project
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()


class Talent(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="talent",
        default=None,
        null=True,
        blank=True,
    )
    skills = models.JSONField(default=list, blank=True, null=True)
    Learning_resources = models.TextField(
        _("Learning Resources"), blank=True, null=True, default=None
    )
    rating = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    no_projects_completed = models.IntegerField(default=0)
    deadline_missed = models.IntegerField(default=0)
    project_cancelled = models.IntegerField(default=0)
    currently_working_on = models.ManyToManyField(
        "Project",
        null=True,
        related_name="current_projects_of_talent",
        default=None,
        blank=True,
    )

    def __str__(self):
        if self.user is not None:
            return self.user.username
        else:
            return str(self.id)


class Mentor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="mentor")
    skills = models.JSONField(default=list, blank=True, null=True, editable=False)
    rating = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    no_projects_mentored = models.IntegerField(default=0)
    currently_mentoring = models.ManyToManyField(
        "Project", null=True, related_name="current_projects_of_mentor"
    )


class University(models.Model):
    name = models.CharField(max_length=255)


class Team(models.Model):
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(Talent, related_name="team_members")
    project = models.ForeignKey(
        Project, on_delete=models.SET_NULL, related_name="teams_project", null=True
    )
    created_at = models.CharField(
        max_length=255,
        default=getdate() + " " + gettime(),
        editable=False,
        blank=True,
        null=True,
    )
    updated_at = models.CharField(
        max_length=255,
        default=getdate() + " " + gettime(),
        editable=False,
        blank=True,
        null=True,
    )
    created_by = models.ManyToManyField(Talent, null=True, related_name="created_teams")
    team_leader = models.ForeignKey(
        Talent, on_delete=models.SET_NULL, null=True, related_name="team_leaders"
    )

    def __str__(self):
        return self.name
