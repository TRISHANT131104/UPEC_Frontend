import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

from ..helpers import getdate, gettime

User = get_user_model()


def __post__path__(instance, filename):
    return "posts/{0}/{1}".format(instance.id, filename)


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    title = models.CharField(max_length=255)
    content = models.TextField()
    images = models.JSONField(default=list, blank=True, null=True, editable=False)
    date = models.CharField(
        max_length=255,
        default=getdate() + " " + gettime(),
        editable=False,
        blank=True,
        null=True,
    )
    file = models.FileField(upload_to=__post__path__, null=True, blank=True)

    def __str__(self):
        return f"{self.project.title} - {self.title}"
