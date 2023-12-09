from  rest_framework import serializers
from .models.community import *
from .models.projects import *
from .models.chat import *
from .models.user import *
from django.contrib.auth import get_user_model

User = get_user_model()

class ChatMsgSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMsg
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username','first_name','last_name','email',"last_login"]

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class GroupMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupMessage
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class TalentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Talent
        fields = '__all__'

class MentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        fields = '__all__'

class ProjectRequirementDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectRequirementDocument
        fields = '__all__'

class TeamSerialzier(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

class WorkflowSerialzier(serializers.ModelSerializer):
    class Meta:
        model = Workflow
        fields = "__all__"