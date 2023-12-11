from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import *

User = get_user_model()

class ChatMsgSerializer(serializers.ModelSerializer):
    """
    Serializer for the ChatMsg model.
    """
    class Meta:
        model = ChatMsg
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model.
    """
    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "email", "last_login"]


class ProjectSerializer(serializers.ModelSerializer):
    """
    Serializer for the Project model.
    """
    class Meta:
        model = Project
        fields = "__all__"


class GroupSerializer(serializers.ModelSerializer):
    """
    Serializer for the Group model.
    """
    class Meta:
        model = Group
        fields = "__all__"


class GroupMessageSerializer(serializers.ModelSerializer):
    """
    Serializer for the GroupMessage model.
    """
    class Meta:
        model = GroupMessage
        fields = "__all__"


class ClientSerializer(serializers.ModelSerializer):
    """
    Serializer for the Client model.
    """
    class Meta:
        model = Client
        fields = "__all__"


class TalentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Talent model.
    """
    class Meta:
        model = Talent
        fields = "__all__"


class MentorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Mentor model.
    """
    class Meta:
        model = Mentor
        fields = "__all__"


class ProjectRequirementDocumentSerializer(serializers.ModelSerializer):
    """
    Serializer for the ProjectRequirementDocument model.
    """
    class Meta:
        model = ProjectRequirementDocument
        fields = "__all__"


class TeamSerializer(serializers.ModelSerializer):
    """
    Serializer for the Team model.
    """
    class Meta:
        model = Team
        fields = "__all__"


class WorkflowSerialzier(serializers.ModelSerializer):
    """
    Serializer for the Workflow model.
    """
    class Meta:
        model = Workflow
        fields = "__all__"
