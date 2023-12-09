from datetime import timedelta
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models.projects import (
    ProjectRequirementDocument,
    Workflow,
    Project,
)
from .llm import data_embeddings, data_embeddings_community


# @receiver(post_save, sender=ProjectRequirementDocument)
# def store_project_embeddings(sender, instance, created, **kwargs):
#     if created:
#         data_embeddings.store_project_requirement_document_embeddings(instance)
#         print("Project embeddings stored")
#     else:
#         data_embeddings.store_project_requirement_document_embeddings(instance)
#         print("Project embeddings already stored")

@receiver(post_save, sender=Project)
def store_project_embeddings(sender, instance, created, **kwargs):
    if instance.prd is not None:
        data_embeddings.store_project_requirement_document_embeddings(instance)
        print("Project embeddings stored")
    else:
        print("Project embeddings already stored")

@receiver(post_save, sender=Workflow)
def update_workflow_status(sender, instance, created, **kwargs):
    if created:
        data_embeddings.update_project_workflow()
        instance.save()
        print("Workflow status updated")
    else:
        print("Workflow status already updated")

@receiver(post_save, sender=User)
def store_user_embeddings(sender, instance, created, **kwargs):
    if created:
        if User.objects.filter(groups__name='Talent').exists():
            data_embeddings_community.store_talent_data(instance.talent)
        elif User.objects.filter(groups__name='Client').exists():
            data_embeddings_community.store_client_data(instance.client)
        elif User.objects.filter(groups__name='Mentor').exists():
            data_embeddings_community.store_mentor_data(instance.mentor)
        print("User embeddings stored")
    else:
        if User.objects.filter(groups__name='Talent').exists():
            data_embeddings_community.update_talent_data(instance.talent)
        elif User.objects.filter(groups__name='Client').exists():
            data_embeddings_community.update_client_data(instance.client)
        elif User.objects.filter(groups__name='Mentor').exists():
            data_embeddings_community.update_mentor_data(instance.mentor)
        print("User embeddings already stored")
