import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

from ..helpers import getdate, gettime

User = get_user_model()


class GroupMessage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    message = models.TextField()
    group = models.ForeignKey("Group", on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at_date = models.CharField(max_length=225, default=getdate(), null=True)
    created_at_time = models.CharField(max_length=225, default=gettime(), null=True)
    ai = models.BooleanField(default=False, null=True, blank=True)


class Group(models.Model):
    grp_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    grp_name = models.CharField(max_length=50)
    created_at_date = models.CharField(max_length=225, default=getdate(), null=True)
    created_at_time = models.CharField(max_length=225, default=gettime(), null=True)
    grp_admin = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="admin",
        null=True,
        default=None,
        blank=True,
    )
    grp_members = models.ManyToManyField(
        User, related_name="members", null=True, default=None, blank=True
    )


class ChatMsg(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="sent_messages"
    )
    receiver = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="received_messages"
    )
    message = models.TextField()
    created_at_date = models.CharField(max_length=225, default=getdate(), null=True)
    created_at_time = models.CharField(max_length=225, default=gettime(), null=True)
    ai = models.BooleanField(default=False, null=True, blank=True)
