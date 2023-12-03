from django.db import models
import uuid
from django.utils import timezone
from ..helpers import getdate,gettime
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.models import User
from .projects import Project

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='client')
    number_of_projects_given = models.IntegerField(default=0)
    number_of_projects_completed = models.IntegerField(default=0)    
    rating = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)


class Talent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='talent')
    skills = models.JSONField(default=list, blank=True, null=True, editable=False)
    rating = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    no_projects_completed = models.IntegerField(default=0)
    deadline_missed = models.IntegerField(default=0)
    project_cancelled = models.IntegerField(default=0)

class Mentor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='mentor')
    skills = models.JSONField(default=list, blank=True, null=True, editable=False)
    rating = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    no_projects_mentored = models.IntegerField(default=0)


class University(models.Model):
    name=models.CharField(max_length=255)

class UserProfile(models.Model):
    Member_Roles = {
        ('Client',Client),
        ('Talent',Talent),
        ('Mentor',Mentor),
    }
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    university = models.ManyToOneRel(University, on_delete=models.CASCADE, related_name='university')
    bio = models.TextField()
    role = models.ForeignKey(max_length=20, choices=Member_Roles, default='Talent')
    currently_working_on = models.ManyToManyField('Project', on_delete=models.SET_NULL, null=True, related_name='current_projects')
    past_projects = models.ManyToManyField('Project', on_delete=models.SET_NULL, null=True, related_name='past_projects')
class Team(models.Model):
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(User, related_name='teams')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='teams')
    created_at = models.CharField(max_length=255, default=getdate() + " " + gettime(), editable=False, blank=True, null=True)
    updated_at = models.CharField(max_length=255, default=getdate() + " " + gettime(), editable=False, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_teams')
    
    def __str__(self):
        return self.name


