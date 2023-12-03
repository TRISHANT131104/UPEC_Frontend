from django.db import models
import uuid
from django.utils import timezone
from ..helpers import getdate,gettime
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin,AbstractUser
from .projects import Project
from django.contrib.auth.models import User
# class User(AbstractBaseUser, PermissionsMixin):
#     role = models.CharField(max_length=20, default='client')

#     class Meta:
#       abstract = False


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='client')
    number_of_projects_given = models.IntegerField(default=0)
    number_of_projects_completed = models.IntegerField(default=0)    
    rating = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    current_projects = models.ManyToManyField('Project', null=True, related_name='current_projects_of_client')


class Talent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='talent')
    skills = models.JSONField(default=list, blank=True, null=True, editable=False)
    rating = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    no_projects_completed = models.IntegerField(default=0)
    deadline_missed = models.IntegerField(default=0)
    project_cancelled = models.IntegerField(default=0)
    currently_working_on = models.ManyToManyField('Project', null=True, related_name='current_projects_of_talent')

class Mentor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='mentor')
    skills = models.JSONField(default=list, blank=True, null=True, editable=False)
    rating = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    no_projects_mentored = models.IntegerField(default=0)
    currently_mentoring = models.ManyToManyField('Project', null=True, related_name='current_projects_of_mentor')

class University(models.Model):
    name=models.CharField(max_length=255)





class Team(models.Model):
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(User, related_name='teams')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='teams')
    created_at = models.CharField(max_length=255, default=getdate() + " " + gettime(), editable=False, blank=True, null=True)
    updated_at = models.CharField(max_length=255, default=getdate() + " " + gettime(), editable=False, blank=True, null=True)
    created_by = models.ManyToManyField(User, null=True, related_name='created_teams')
    def __str__(self):
        return self.name