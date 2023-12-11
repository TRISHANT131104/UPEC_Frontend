from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from ..models import *
from ..serializers import *
import json

class __create__project__(APIView):
    """
    API view for creating a project.

    This view allows clients to create a new project by providing the necessary information such as title, description,
    bid price, and related tech stacks. The project is associated with the authenticated client user.

    Args:
        request (HttpRequest): The HTTP request object.

    HTTP Methods:
        - POST: Create a new project.

    Request Parameters:
        - title (str): The title of the project.
        - description (str): The description of the project.
        - bid_price (float): The bid price for the project.
        - related_techstacks (list): A list of related tech stacks for the project.
        - project_doc (file): Optional. The project documentation file.

    Returns:
        - If the project is created successfully, returns a JSON response with the project details.
        - If the user is not a client, returns a JSON response with an error message.
    """
    def post(self, request):
        # Create a project
        user = request.user
        # Check if user is a client
        is_client = Client.objects.filter(user=user).exists()
        if is_client:
            # Get the client
            client = Client.objects.get(user=user)
            # Create a project
            project = Project.objects.create(
                created_by=client,
                title=request.data["title"],
                description=request.data["description"],
                bid_price=request.data["bid_price"],
                related_techstacks=request.data["related_techstacks"],
            )
            if request.data["project_doc"]:
                project.project_doc = request.data["project_doc"]
            project.save()
        else:
            return Response({"error": "You are not a client"})
        

class __get__all__projects__(APIView):
    """
    API view to retrieve all projects.
    """

    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        for i in serializer.data:
            i["created_by"] = ClientSerializer(
                Client.objects.get(id=i["created_by"])
            ).data
            i["created_by"]["user"] = UserSerializer(
                User.objects.get(id=i["created_by"]["user"])
            ).data
        return Response(serializer.data)
    
class __get__each__project__(APIView):
    """
    API view to retrieve data for a specific project.

    Args:
        request (HttpRequest): The HTTP request object.
        pk (int): The primary key of the project.

    HTTP Methods:
        - GET: Retrieve the project data.

    Returns:
        Response: The HTTP response containing the project data.

    Raises:
        Project.DoesNotExist: If the project with the given primary key does not exist.
        Client.DoesNotExist: If the client associated with the project does not exist.
        User.DoesNotExist: If the user associated with the client does not exist.
    """

    def get(self, request, pk):
        
        # Get the project data
        try:
            # Get the project
            project = Project.objects.get(id=pk)
        except Project.DoesNotExist:
            return Response({"error": "Project not found"}, status=404)
        project_data = ProjectSerializer(project).data

        # Get the client data
        try:
            # Get the client
            client = Client.objects.get(id=project_data["created_by"])
        except Client.DoesNotExist:
            return Response({"error": "Client not found"}, status=404)
        client_data = ClientSerializer(client).data
        project_data["created_by"] = client_data

        # Get the user data
        try:
            # Get the user
            user = User.objects.get(id=client_data["user"])
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=404)
        user_data = UserSerializer(user).data
        project_data["created_by"]["user"] = user_data

        # Get the project workflow
        if project_data["workflow"] is not None:
            project_data["workflow"] = WorkflowSerialzier(Workflow.objects.get(id=project_data["workflow"])).data

        # Get the project requirement document
        if project_data['prd'] is not None:
            project_data["prd"] = ProjectRequirementDocumentSerializer(ProjectRequirementDocument.objects.get(id=project_data["prd"])).data

        # Get the project management information
        if project_data["project_management"] is not None or project_data['project_management']=="":
            project_data["project_management"] = json.loads(project_data["project_management"])

        # Get the project team details
        team = Team.objects.filter(project=project)
        if team.exists():
            team = team.first()
            team_serializer = TeamSerializer(team)
            project_data["team"] = team_serializer.data
            project_data["team"]["members"] = [UserSerializer(Talent.objects.get(id=member_id).user).data for member_id in project_data["team"]["members"]]
        else:
            project_data["team"] = None
        return Response(project_data)


class __get__details__of__project__(APIView):
    """
    API view to get the details of a project of that user.
    """
    def get(self, request, pk):
        # Get the details of the project
        user = request.user
        # Check if the person accessing it is in the Team and the Team is in the project
        project = Project.objects.get(id=pk)
        team = Team.objects.filter(project=project)
        if team:
            team = team[0]
            if user in team.members.all():
                serializer = ProjectSerializer(project)
                return Response(serializer.data)
            else:
                return Response({"error": "You are not a member of this project"})
        else:
            return Response({"error": "No team found for this project"})



class __get__user__data__(APIView):
    """
    API view to get user data based on their role (Client, Talent, or Mentor).

    Args:
        request (HttpRequest): The HTTP request object.
        pk (int): The primary key of the user.

    HTTP Methods:
        - GET: Retrieve the user data.

    Returns:
        Response: The response containing the user data.

    Raises:
        User.DoesNotExist: If the user with the given primary key does not exist.
    """
    def get(self, request, pk):
        user = User.objects.get(id=pk)
        # Get user data
        try:
            # Check if users is a client, talent/mentor and send the data along with the user data
            is_client = Client.objects.filter(user=user).exists()
            is_talent = Talent.objects.filter(user=user).exists()
            is_mentor = Mentor.objects.filter(user=user).exists()
            if is_client:
                client = Client.objects.get(user=user)
                serializer = ClientSerializer(client)
                # Also add the user details to the client data
                user_serializer = UserSerializer(user)
                user_data = user_serializer.data
                user_data.update(serializer.data)
                user_data.update({"role": "Client"})
                return Response(user_data)
            elif is_talent:
                talent = Talent.objects.get(user=user)
                serializer = TalentSerializer(talent)
                user_serializer = UserSerializer(user)
                user_data = user_serializer.data
                user_data.update(serializer.data)
                user_data.update({"role": "Talent"})
                return Response(user_data)
            elif is_mentor:
                mentor = Mentor.objects.get(user=user)
                serializer = MentorSerializer(mentor)
                user_serializer = UserSerializer(user)
                user_data = user_serializer.data
                user_data.update(serializer.data)
                user_data.update({"role": "Mentor"})
                return Response(user_data)
            else:
                # Handle the case when the user doesn't have any role
                return Response({"error": "User has no role"})
        except User.DoesNotExist:
            return Response({"error": "User not found"})
        
class __get__users__ongoing__projects__(APIView):
    """
    API view to get ongoing projects for a user.

    Args:
        request (HttpRequest): The HTTP request object.
        pk (int): The primary key of the user.

    HTTP Methods:
        - GET: Retrieve the ongoing projects.

    Returns:
        JsonResponse or Response: JSON response containing the ongoing projects.

    Raises:
        User.DoesNotExist: If the user with the given primary key does not exist.
    """

    def get(self, request, pk):
        user = User.objects.get(id=pk)
        is_talent = Talent.objects.filter(user=user).exists()
        is_client = Client.objects.filter(user=user).exists()
        if is_talent:
            talent = Talent.objects.get(user=user)
            team = Team.objects.filter(members=talent)
            serializer = TeamSerializer(team, many=True)
            projects = []
            for i in serializer.data:
                projects.append(ProjectSerializer(Project.objects.get(id=i['project'])).data)
            return JsonResponse(projects, safe=False)
        elif is_client:
            client = Client.objects.get(user=user)
            project = Project.objects.filter(created_by=client)
            serializer = ProjectSerializer(project, many=True)
            return Response(serializer.data)
        else:
            return Response("You Are Not a Talent, You Cannot Access it")
        
class __get__team__related__to__project__(APIView):
    """
    API view to get the team related to a project.

    Args:
        request (HttpRequest): The HTTP request object.
        pk (int): The primary key of the project.

    HTTP Methods:
        - GET: Retrieve the team related to the project.

    Returns:
        Response: The response containing the team data.

    Raises:
        Project.DoesNotExist: If the project with the given primary key does not exist.
    """

    def get(self, request, pk):
        project = Project.objects.get(id=pk)
        team = Team.objects.filter(project=project)
        if team.exists():
            team = team.first()
            serializer = TeamSerializer(team)
            return Response(serializer.data)
        else:
            return Response('team does not exist')
