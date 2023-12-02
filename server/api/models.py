from django.db import models
import uuid
from django.utils import timezone
from .helpers import getdate,gettime
from django.contrib.auth.models import User

def __project__image__path__(instance, filename):
    return 'project_images/{0}/{1}'.format(instance.id, filename)

def __prd__file__path__(instance, filename):
    return 'prds/{0}/{1}'.format(instance.id, filename)

def __learning__resource__path__(instance, filename):
    return 'learning_resources/{0}/{1}'.format(instance.id, filename)

def __post__path__(instance, filename):
    return 'posts/{0}/{1}'.format(instance.id, filename)

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='client')

class Talent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='talent')
    skills = models.JSONField(default=list, blank=True, null=True, editable=False)
    rating = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)


class ProjectStatus(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.CharField(max_length=255, default=getdate() + " " + gettime(), editable=False, blank=True, null=True)
    end_date = models.CharField(max_length=255, default=getdate() + " " + gettime(), editable=False, blank=True, null=True)
    bid_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.ForeignKey(ProjectStatus, on_delete=models.SET_NULL, null=True)
    project_image = models.ImageField(upload_to=__project__image__path__, null=True, blank=True)
    prd = models.FileField(upload_to=__prd__file__path__, null=True, blank=True)
    milestones = models.ManyToManyField('Milestone', related_name='projects', blank=True)
    learning_resource = models.ForeignKey('LearningResource', on_delete=models.SET_NULL, null=True)
    related_techstacks = models.JSONField(default=list, blank=True, null=True, editable=False)
    created_at = models.CharField(max_length=255, default=getdate() + " " + gettime(), editable=False, blank=True, null=True)
    updated_at = models.CharField(max_length=255, default=getdate() + " " + gettime(), editable=False, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_projects')
    def __str__(self):
        return self.title

class Milestone(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()

    def __str__(self):
        return self.name

class ProjectProgressReport(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='progress_reports')
    report = models.TextField()
    date = models.DateField(auto_now_add=True)
    milestone_accomplished = models.ForeignKey(Milestone, on_delete=models.SET_NULL, null=True, blank=True)
    project_completion_percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f'{self.project.title} - {self.date}'

class LearningResource(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    url = models.URLField()
    date = models.DateField(auto_now_add=True)
    file = models.FileField(upload_to=__learning__resource__path__, null=True, blank=True)

    def __str__(self):
        return self.name

# Assuming these functions are defined in helpers.py

class ProjectMembers(models.Model):
    Member_Roles = {
        ('Member','Member'),
        ('Leader','Leader'),
        ('Client','Client'),
        ('Mentor','Mentor'),
    }
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='members')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    role = models.CharField(max_length=20, choices=Member_Roles, default='Member')

    def __str__(self):
        return f'{self.project.title} - {self.user.email}'
    
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=255)
    content = models.TextField()
    date = models.CharField(max_length=255, default=getdate() + " " + gettime(), editable=False, blank=True, null=True)
    file = models.FileField(upload_to=__post__path__, null=True, blank=True)

    def __str__(self):
        return f'{self.project.title} - {self.title}'