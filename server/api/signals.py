from datetime import timedelta

from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from .models.projects import (
    ProjectRequirementDocument
)
from .llm import data_embeddings


@receiver(post_save, sender=ProjectRequirementDocument)
def store_project_embeddings(sender, instance, created, **kwargs):
    if created:
        data_embeddings.store_project_embeddings(instance)
        print("Project embeddings stored")
    else:
        print("Project embeddings already stored")

# @receiver(post_save, sender=Workflow)
# def update_workflow_status(sender, instance, created, **kwargs):
#     if created:
#         data_embeddings.update_project_workflow()
#         instance.save()
#         print("Workflow status updated")
#     else:
#         print("Workflow status already updated")
