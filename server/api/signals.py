import logging
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .llm import data_embeddings, data_embeddings_community
from .models import Project

logger = logging.getLogger(__name__)

@receiver(post_save, sender=Project)
def store_project_embeddings(sender, instance, created, **kwargs):
    """
    Store project embeddings.
    """
    try:
        if instance.prd is not None and instance.workflow is None:
            data_embeddings.store_project_requirement_document_embeddings(instance)
            logger.info("Project embeddings stored")
        else:
            logger.info("Project embeddings already stored")
    except Exception as e:
        logger.error(f"Error storing project embeddings: {str(e)}")


@receiver(post_save, sender=User)
def store_user_embeddings(sender, instance, created, **kwargs):
    """
    Store or update user embeddings based on the user's group.
    """
    if created:
        if instance.groups.filter(name='Talent').exists():
            store_talent_embeddings(instance.talent)
        elif instance.groups.filter(name='Client').exists():
            store_client_embeddings(instance.client)
        elif instance.groups.filter(name='Mentor').exists():
            store_mentor_embeddings(instance.mentor)
        logger.info("User embeddings stored")
    else:
        if instance.groups.filter(name='Talent').exists():
            update_talent_embeddings(instance.talent)
        elif instance.groups.filter(name='Client').exists():
            update_client_embeddings(instance.client)
        elif instance.groups.filter(name='Mentor').exists():
            update_mentor_embeddings(instance.mentor)
        logger.info("User embeddings already stored")

def store_talent_embeddings(talent):
    """
    Store talent embeddings.
    """
    data_embeddings_community.store_talent_data(talent)

def store_client_embeddings(client):
    """
    Store client embeddings.
    """
    data_embeddings_community.store_client_data(client)

def store_mentor_embeddings(mentor):
    """
    Store mentor embeddings.
    """
    data_embeddings_community.store_mentor_data(mentor)

def update_talent_embeddings(talent):
    """
    Update talent embeddings.
    """
    data_embeddings_community.update_talent_data(talent)

def update_client_embeddings(client):
    """
    Update client embeddings.
    """
    data_embeddings_community.update_client_data(client)

def update_mentor_embeddings(mentor):
    """
    Update mentor embeddings.
    """
    data_embeddings_community.update_mentor_data(mentor)