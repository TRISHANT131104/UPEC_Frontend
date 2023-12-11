import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from ..llm import *
from ..models import *
from ..serializers import *
from .get_data_views import __get__users__ongoing__projects__


class __send__generated__prd__(APIView):
    """
    Send the AI generated prd to the client
    """
    def post(self, request):
        # Get the user from the request data ID
        user = get_object_or_404(User, id=request.data['id'])
        # Check if the user is a client
        is_client = Client.objects.filter(user=user).exists()
        if is_client:
            # Get the client object based on the provided user ID
            client = get_object_or_404(Client, user=user)
            # Get the project object based on the provided project ID
            project = get_object_or_404(Project, id=request.data['project_id'])
            # Check if the client is the owner of the project
            if project.created_by == client:
                # call the llm function to generate the prd
                prd = generate_prd(project)
                serializer = ProjectRequirementDocumentSerializer(get_object_or_404(ProjectRequirementDocument, id=prd))
                # Return the PRD JSON response
                return JsonResponse(
                    {"success": "PRD generated successfully", "data": serializer.data}
                )
            else:
                # Return an error if the client is not the owner of the project
                return Response({"error": "You are not the owner of this project"})
        else:
            # Return an error if the user is not a client
            return Response({"error": "You are not a client"})


class __send__generated__workflow__(APIView):
    """
    Send the AI generated workflow to the team for a project
    """
    def post(self, request):
        # Get the user ID from the request data
        user_id = request.data["id"]
        if user_id is not None:
            # Get the user object based on the provided user ID
            user = get_object_or_404(User, id=user_id)
            # Check if the user is a talent
            is_talent = Talent.objects.filter(user=user).exists()
            if is_talent:
                # Get the project ID from the request data
                project_id = request.data["project_id"]
                # Get the project object based on the provided project ID
                project = get_object_or_404(Project, id=project_id)
                # Retrieve the team associated with the project
                team = Team.objects.filter(project=project)

                if team.exists():
                    # call the llm function to generate the workflow
                    workflow = make_workflow(project)
                    # Update the project workflow in the vector database
                    data_embeddings.update_project_workflow(project)
                    return JsonResponse(
                        {"success": "Workflow generated successfully", "data": workflow}
                    )
                else:
                    # Return an error if the user is not a team leader
                    return JsonResponse(
                        {"error": "You are not a team member of this project"}
                    )
            else:
                # Return an error if the user is not a talent
                return JsonResponse({"error": "You are not a talent"})
        else:
            # Return an error if the user ID is not provided in the request data
            return JsonResponse({"error": "User ID is not provided in the request data"})


class __project__management__(APIView):
    """
    Send the AI generated project management report to the team for a project
    """
    def post(self, request):
        # Get the user ID from the request data
        user_id = request.data["id"]
        if user_id is not None:
            # Get the user object based on the provided user ID
            user = get_object_or_404(User, id=user_id)
            # Check if the user is a talent
            is_talent = Talent.objects.filter(user=user).exists()
            if is_talent:
                # Get the project object from the request data
                project = Project.objects.get(id=request.data["project_id"])
                # Get the team object based on the provided project ID
                team = Team.objects.filter(project=project)
                if team.exists():
                    # call the llm function to generate the project management report
                    management = generate_management(team, project)
                    # Update the project management in the project model
                    project.project_management = management
                    # Save the project
                    project.save()
                    return Response(
                        {
                            "success": "Project management generated successfully",
                            "data": json.loads(management),
                        }
                    )
                else:
                    # Return an error if the user is not a team leader
                    return Response(
                        {"error": "You are not a team leader of this project"}
                    )
            else:
                # Return an error if the user is not a talent
                return Response({"error": "Error occured"})
        else:
            # Return an error if the user ID is not provided in the request data
            return Response({"error": "User ID is not provided in the request data"})


class __learning__resource__(APIView):
    """
    Send the AI generated learning resources to the team for a project
    """
    def post(self, request):
        # Get the user ID from the request data
        user = User.objects.get(id=request.data["id"])
        # Check if user is a talent
        is_talent = Talent.objects.filter(user=user).exists()

        if is_talent:
            # Get the talent
            talent = Talent.objects.filter(user=user)
            # Get the project
            project = Project.objects.get(id=request.data["project_id"])
            # Get the team associated with the project
            team = Team.objects.filter(project=project)

            if team.exists():
                # call the llm function to generate the learning resources
                learning_resource_output = learning_resource(project)
                project.Learning_resources = learning_resource_output
                project.save()
                return Response(
                    {
                        "success": "Learning Resources generated successfully",
                        "data": learning_resource_output,
                    }
                )
            else:
                # Return an error if the team is not related to the project
                return Response({"error": "You are not a team member of this project"})
            
        else:
            # Return an error if the user is not a talent
            return Response({"error": "You are not a talent"})


class __learning__resources__for__talents__(APIView):
    """
    Send the AI generated learning resources for a particular talent
    """
    def post(self, request):
        # Generate the learning resources for the talent
        user = User.objects.get(id=request.data["id"])
        # Check if user is a talent
        is_talent = Talent.objects.filter(user=user).exists()
        if is_talent:
            # Get the talent
            talent = Talent.objects.get(user=user)
            # Get the project
            projects = []
            
            teams = Team.objects.filter(members=talent)
            # Call the get method of the view
            projects = []
            for team in teams:
                projects.append(team.project)

            # call the llm function to generate the learning resources for a talent
            learning_resource = generate_learning_reasources(talent, projects)
            print(talent)
            talent.Learning_resources = learning_resource
            talent.save()
            return JsonResponse(
                {
                    "success": "Learning resources generated successfully",
                    "data": learning_resource,
                }
            )
        else:
            return Response({"error": "You are not a talent"})



class __get__project__recommendations__(APIView):
    """
    Get the AI generated project recommendations for a talent
    """
    def post(self, request):
        # get user object from the request data ID
        user = User.objects.get(id=request.data["id"])

        # Check if user is a talent
        is_talent = Talent.objects.filter(user=user).exists()
        if is_talent:
            # Get the talent
            talent_instance = Talent.objects.get(user=user)
            # Get the skills of the talent
            skill = []
            for i in talent_instance.skills:
                skill.append(i)
            # call the llm function to generate the project recommendations for a talent
            project_ids = project_recomendation(skill)
            # Get the project objects based on the recieved project IDs
            response=[]
            for i in project_ids:
                project = Project.objects.get(id=i)
                serializer = ProjectSerializer(project)
                response.append(serializer.data)
            return JsonResponse(project_ids, safe=False)
        else:
            return Response({"error": "You are not a talent"})

