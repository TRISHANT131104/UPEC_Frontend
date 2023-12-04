from django.db import models
import uuid
from django.utils import timezone
from ..helpers import getdate,gettime
from django.contrib.auth import get_user_model
from .chat import *

User = get_user_model()
def __prd__file__path__(instance, filename):
    return 'prds/{0}/{1}'.format(instance.id, filename)

def __prd__file__path__(instance, filename):
    return 'prds/{0}/{1}'.format(instance.id, filename)

def __learning__resource__path__(instance, filename):
    return 'learning_resources/{0}/{1}'.format(instance.id, filename)

class ProjectRequirementDocument(models.Model):
    project_overview = models.TextField()
    original_requirements = models.TextField()
    project_goals = models.TextField()
    user_stories = models.TextField()
    system_architecture = models.TextField()
    requirements_analysis = models.TextField()
    requirement_pool = models.TextField()
    ui_ux_design = models.TextField()
    development_methodology = models.TextField()
    security_measures = models.TextField()
    testing_strategy = models.TextField()
    scalability_and_performance = models.TextField()
    deployment_plan = models.TextField()
    maintenance_and_support = models.TextField()
    risks_and_mitigations = models.TextField()
    compliance_and_regulations = models.TextField()
    budget_and_resources = models.TextField()
    timeline_and_milestones = models.TextField()
    communication_plan = models.TextField()
    anything_unclear = models.TextField()
    
class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.CharField(max_length=255, default=getdate() + " " + gettime(), editable=True, blank=True, null=True)
    end_date = models.CharField(max_length=255, default=getdate() + " " + gettime(), editable=True, blank=True, null=True)
    bid_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, default='Open')
    project_doc = models.FileField(upload_to=__prd__file__path__, null=True, blank=True)
    prd = models.OneToOneField(ProjectRequirementDocument, related_name="PRD", on_delete=models.SET_NULL, null=True, blank=True)
    learning_resource = models.ForeignKey('LearningResource', on_delete=models.SET_NULL, null=True,blank=True)
    workflow = models.TextField(default=None, blank=True, null=True)
    related_techstacks = models.JSONField(default=list, blank=True, null=True, editable=False)
    created_at = models.CharField(max_length=255, default=getdate() + " " + gettime(), editable=False, blank=True, null=True)
    updated_at = models.CharField(max_length=255, default=getdate() + " " + gettime(), editable=False, blank=True, null=True)
    created_by = models.ForeignKey(User,null=True,default=None,blank=True,related_name='created_projects',on_delete=models.SET_NULL)
    chat_group_id = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True)
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
    

