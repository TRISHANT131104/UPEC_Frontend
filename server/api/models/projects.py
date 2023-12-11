import uuid
from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from ..helpers import getdate, gettime
from .chat import *

User = get_user_model()


def __prd__file__path__(instance, filename):
    return "prds/{0}/{1}".format(instance.id, filename)


def __learning__resource__path__(instance, filename):
    return "learning_resources/{0}/{1}".format(instance.id, filename)


class ProjectRequirementDocument(models.Model):
    project_overview = models.TextField()
    original_requirements = models.TextField()
    project_goals = models.TextField()
    user_stories = models.TextField()
    system_architecture = models.TextField()
    tech_stacks = models.TextField()
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


class Workflow(models.Model):
    description = models.TextField()


class Client(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="client",
        default=None,
        null=True,
        blank=True,
    )
    number_of_projects_given = models.IntegerField(default=0)
    number_of_projects_completed = models.IntegerField(default=0)
    rating = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    current_projects = models.ManyToManyField(
        "Project",
        related_name="current_projects_of_client",
        null=True,
        default=None,
        blank=True,
    )


class Project(models.Model):
    status_options = {
        (_("Open"),_("Open")),
        (_("OnGoing"),_("OnGoing")),
        (_("inBid"),_("inBid")),
        (_("Closed"),_("Closed")),
    }
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.CharField(
        max_length=255,
        default=getdate() + " " + gettime(),
        editable=True,
        blank=True,
        null=True,
    )
    end_date = models.CharField(
        max_length=255,
        default=getdate() + " " + gettime(),
        editable=True,
        blank=True,
        null=True,
    )
    bid_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, default='Open',choices=status_options)
    project_doc = models.FileField(
        upload_to=__prd__file__path__, null=True, blank=True, default=None
    )
    prd = models.ForeignKey(
        ProjectRequirementDocument,
        related_name="PRD",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None,
    )
    Learning_resources = models.TextField(
        _("Learning Resources"), blank=True, null=True, default=None
    )
    related_techstacks = models.JSONField(default=list, blank=True, null=True)
    project_management = models.TextField(default=None, null=True, blank=True)
    project_timeline = models.JSONField(default=None, null=True, blank=True)
    workflow = models.ForeignKey(
        Workflow,
        related_name="workflow",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None,
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
    created_by = models.ForeignKey(
        Client,
        null=True,
        default=None,
        blank=True,
        related_name="created_projects",
        on_delete=models.SET_NULL,
    )
    chat_group_id = models.ForeignKey(
        Group, on_delete=models.SET_NULL, null=True, blank=True, default=None
    )


class Milestone(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()

    def __str__(self):
        return self.name


class ProjectProgressReport(models.Model):
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="progress_reports"
    )
    report = models.TextField()
    date = models.DateField(auto_now_add=True)
    milestone_accomplished = models.ForeignKey(
        Milestone, on_delete=models.SET_NULL, null=True, blank=True
    )
    project_completion_percentage = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True
    )

    def __str__(self):
        return f"{self.project.title} - {self.date}"


# Assuming these functions are defined in helpers.py


class ProjectMembers(models.Model):
    Member_Roles = {
        ("Member", "Member"),
        ("Leader", "Leader"),
        ("Client", "Client"),
        ("Mentor", "Mentor"),
    }
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="members"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="projects")
    role = models.CharField(max_length=20, choices=Member_Roles, default="Member")

    def __str__(self):
        return f"{self.project.title} - {self.user.email}"
