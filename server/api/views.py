import json

from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from rest_framework.views import APIView

from .llm import *
from .models import *
from .serializers import *
from .utils import *

# Views for handling different API endpoints


class __get__all__projects__(APIView):
    # Get all projects with additional data about their creators
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


class __get__group__messages__(APIView):
    def post(self, request):
        # Get user, get the group id from pk, query the group messages and return the messages of that group if ai=True
        user = User.objects.get(id=request.data["sender"])
        grp_id = request.data["receiver"]
        group = Group.objects.get(grp_id=grp_id)
        if user in group.grp_members.all():
            messages = GroupMessage.objects.filter(group=group)
            serializer = GroupMessageSerializer(messages, many=True)
            response = []
            for i in serializer.data:
                data = {
                    "sender": User.objects.get(id=i["sender"]).username,
                    "id": i["id"],
                    "message": i["message"],
                    "ai": i["ai"],
                    "created_at_date": i["created_at_date"],
                    "created_at_time": i["created_at_time"],
                }
                response.append(data)
            return JsonResponse(response, safe=False)
        else:
            return Response({"error": "You are not a member of this group"})


class __get__personal__chat__(APIView):
    def post(self, request):
        # Get user chats related to the user and return the messages of that user if ai = False
        user = User.objects.get(id=request.data["sender"])
        receiver = User.objects.get(id=request.data["receiver"])
        ai = request.data["ai"]
        messages = ChatMsg.objects.filter(
            sender=user, receiver=receiver, ai=ai
        ).order_by("created_at_date", "created_at_time") | ChatMsg.objects.filter(
            receiver=user, sender=receiver, ai=ai
        ).order_by(
            "created_at_date", "created_at_time"
        )
        serializer = ChatMsgSerializer(messages, many=True)
        response = []
        for i in serializer.data:
            data = {
                "sender": User.objects.get(id=i["sender"]).username,
                "receiver": User.objects.get(id=i["receiver"]).username,
                "id": i["id"],
                "message": i["message"],
                "ai": i["ai"],
                "created_at_date": i["created_at_date"],
                "created_at_time": i["created_at_time"],
            }
            response.append(data)
        return JsonResponse(response, safe=False)


class __get__ai__messages__(APIView):
    def __get__ai__messages__(request, pk):
        # Get user chats related to the user and return the messages of that user if ai = True
        user = request.user
        receiver = User.objects.get(id=pk)
        messages = ChatMsg.objects.filter(sender=user, receiver=user, ai=True)
        serializer = ChatMsgSerializer(messages, many=True)
        return Response(serializer.data)


class __get__user__data__(APIView):
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
                return Response({"error": "User not found"})
        except:
            return Response({"error": "User not found"})


class __get__users__recent__chat__(APIView):
    def get(self, request):
        # Get users recent private/group chat
        user = request.user
        # Get the recent chat of the user
        recent_chat = ChatMsg.objects.filter(sender=user).order_by(
            "+created_at_date", "+created_at_time"
        )
        serializer = ChatMsgSerializer(recent_chat, many=True)
        recent_group_chat = GroupMessage.objects.filter(sender=user).order_by(
            "+created_at_date", "+created_at_time"
        )
        group_serializer = GroupMessageSerializer(recent_group_chat, many=True)
        # Combine both group and recent chat and order them again
        chat = list(serializer.data) + list(group_serializer.data)
        chat.sort(
            key=lambda x: (x["created_at_date"], x["created_at_time"]), reverse=True
        )
        return JsonResponse(chat, safe=False)


class __create__project__(APIView):
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


def __generate__prd__(
    project_title, project_desc, project_start_date, project_end_date
):
    response = {
        "project_overview": None,
        "project_goals": None,
        "original_requirements": None,
        "user_stories": None,
        "system_architecture": None,
        "requirements_analysis": None,
        "ui_ux_design": None,
        "development_methodology": None,
        "security_measures": None,
        "testing_strategy": None,
        "scalability_and_performance": None,
        "deployment_plan": None,
        "maintenance_and_support": None,
        "risks_and_mitigations": None,
        "compliance_and_regulations": None,
        "budget_and_resources": None,
        "timeline_and_milestones": None,
        "communication_plan": None,
        "anything_unclear": None,
    }
    """
    call your llm and make it predict the prd using the above parameters
    return a dictionary of all the parameters in the predicted prd similar to the ProjectRequirementDocument model
    """

    return response


class __send__generated__prd__(APIView):
    def post(self, request):
        # Send the generated prd to the client
        user = User.objects.get(id=request.data["id"])
        # Check if user is a client
        is_client = Client.objects.filter(user=user).exists()
        if is_client:
            # Get the client
            client = Client.objects.get(user=user)
            print(client)
            # Get the project
            project = Project.objects.get(id=request.data["project_id"])
            # Check if the client is the owner of the project
            if project.created_by == client:
                # Generate the prd
                prd = generate_prd_button_clicked(project)
                return JsonResponse(
                    {"success": "PRD generated successfully", "data": prd}
                )
            else:
                return Response({"error": "You are not the owner of this project"})
        else:
            return Response({"error": "You are not a client"})


class __get__details__of__project__(APIView):
    def get(self, request, pk):
        # Get the details of the project
        user = request.user
        # Check if user is a client
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


class __client__accept__bid__(APIView):
    def post(self, request):
        # Accept the bid of the talent
        user = request.user
        data = request.data
        # Check if user is a client

        is_client = Client.objects.filter(user=user).exists()
        if is_client:
            # Get the client
            client = Client.objects.get(user=user)
            # Get the project
            project = Project.objects.get(id=request.data["project_id"])
            # Chech if the client is the owner of the project
            if project.created_by == client:
                # Filter team with the given team id
                team = Team.objects.get(id=data["team_id"])
                team.project = project
                team.save()
                # Get the team members
                team_members = list(team.members.all())
                # Create a group
                group = Group.objects.create(
                    grp_name=data["team_name"],
                    grp_admin=client,
                    grp_members=team_members,
                )
                group.save()

                # Update the project
                project.chat_group_id = group
                project.save()
            else:
                return Response({"error": "You are not the owner of this project"})
        else:
            return Response({"error": "You are not a client"})


def generate_workflow(title, desc, timeline, students_info):
    """
    call your llm and make it predict the workflow using the above parameters
    return a dictionary of all the parameters in the predicted workflow similar to the Workflow model
    """
    response = {}
    return response


class __send__generated__workflow__(APIView):
    def post(self, request):
        # Get the user ID from the request data
        user_id = request.data.get("id")

        if user_id is not None:
            # Get the user object based on the provided user ID
            user = get_object_or_404(User, id=user_id)
            # Check if the user is a talent
            is_talent = Talent.objects.filter(user=user).exists()

            if is_talent:
                # Get the project ID from the request data
                project_id = request.data.get("project_id")
                # Get the project object based on the provided project ID
                project = get_object_or_404(Project, id=project_id)
                # Retrieve the team associated with the project
                team = Team.objects.filter(project=project)

                if team.exists():
                    # Generate the workflow
                    workflow = make_workflow(project)
                    # Update the project workflow in data embeddings
                    data_embeddings.update_project_workflow(project)
                    return JsonResponse(
                        {"success": "Workflow generated successfully", "data": workflow}
                    )
                else:
                    # Return an error if the user is not a team leader
                    return Response(
                        {"error": "You are not the team leader of this project"}
                    )
            else:
                # Return an error if the user is not a talent
                return Response({"error": "You are not a talent"})
        else:
            # Return an error if the user ID is not provided in the request data
            return Response({"error": "User ID is not provided in the request data"})


class __project__management__(APIView):
    def post(self, request):
        # Get the user ID from the request data
        user_id = request.data.get("id")
        data = request.data

        if user_id is not None:
            # Get the user object based on the provided user ID
            user = get_object_or_404(User, id=user_id)
            # Check if the user is a talent
            is_talent = Talent.objects.filter(user=user).exists()

            if is_talent:
                # Get the project object from the request data
                project = Project.objects.get(id=data["project_id"])
                # Get the team object based on the provided project ID
                team = Team.objects.filter(project=project)

                if team.exists():
                    # Generate the project management
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
    def post(self, request):
        # Get the user ID from the request data
        user = User.objects.get(id=request.data["id"])
        data = request.data
        # Check if user is a talent
        is_talent = Talent.objects.filter(user=user).exists()

        if is_talent:
            # Get the talent
            talent = Talent.objects.filter(user=user)
            # Get the project
            project = Project.objects.get(id=data["project_id"])
            # Get the team associated with the project
            team = Team.objects.filter(project=project)

            if team:
                team = team[0]
                learning_resource_output = learning_resource(talent, project)
                print("learning resource output", learning_resource_output)
                project.Learning_resources = learning_resource_output
                project.save()
                return Response(
                    {
                        "success": "Learning Resources generated successfully",
                        "data": learning_resource_output,
                    }
                )
            else:
                return Response({"error": "You are not a team"})


class __get__each__project__(APIView):
    def get(self, request, pk):
        try:
            # Get the project
            project = Project.objects.get(id=pk)
        except Project.DoesNotExist:
            return Response({"error": "Project not found"}, status=404)
        # Get the project data
        project_data = ProjectSerializer(project).data

        try:
            # Get the client
            client = Client.objects.get(id=project_data["created_by"])
        except Client.DoesNotExist:
            return Response({"error": "Client not found"}, status=404)
        # Get the client data
        client_data = ClientSerializer(client).data
        project_data["created_by"] = client_data

        try:
            # Get the user
            user = User.objects.get(id=client_data["user"])
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=404)
        # Get the user data
        user_data = UserSerializer(user).data
        project_data["created_by"]["user"] = user_data
        if project_data["workflow"] is not None:
            project_data["workflow"] = WorkflowSerialzier(
                Workflow.objects.get(id=project_data["workflow"])
            ).data
        if project_data["prd"] is not None:
            project_data["prd"] = ProjectRequirementDocumentSerializer(
                ProjectRequirementDocument.objects.get(id=project_data["prd"])
            ).data
        if project_data["project_management"] is not None:
            project_data["project_management"] = json.loads(
                project_data["project_management"]
            )
        return Response(project_data)


class __learning__resources__for__talents__(APIView):
    def post(self, request):
        # Generate the learning resources for the talent
        user = request.user
        # Check if user is a talent
        is_talent = Talent.objects.filter(user=user).exists()
        if is_talent:
            # Get the talent
            talent = Talent.objects.get(user=user)
            # Get the project
            project = Project.objects.get(id=request.data["project_id"])
            # Generate the workflow
            learning_resource = generate_learning_reasources(talent, project)
            return JsonResponse(
                {
                    "success": "Learning resources generated successfully",
                    "data": learning_resource,
                }
            )
        else:
            return Response({"error": "You are not a talent"})


class __get__direct__chat__users__(APIView):
    def get(self, request, pk):
        user = User.objects.get(id=pk)
        users_chats = ChatMsg.objects.filter(sender=user) | ChatMsg.objects.filter(
            receiver=user
        )
        print(users_chats)
        serializer = ChatMsgSerializer(users_chats, many=True)
        response = []
        print(serializer.data)
        for i in serializer.data:
            print("i ", i["sender"], i["receiver"])
            if i["sender"] not in response:
                response.append(i["sender"])
            if i["receiver"] not in response:
                response.append(i["receiver"])
        print("response", response)
        direct_chat_users = []
        for i in response:
            direct_chat_users.append(UserSerializer(User.objects.get(id=i)).data)
        print(direct_chat_users)
        return JsonResponse(direct_chat_users, safe=False)


class __get__project__related__groups__(APIView):
    def get(self, request, pk):
        user = User.objects.get(id=pk)
        team = Team.objects.filter(members=pk)
        serializer = TeamSerialzier(team, many=True)
        project_groups = []
        for i in serializer.data:
            if i["project"] not in project_groups:
                project_groups.append(i["project"])
        response = []
        for i in project_groups:
            response.append(
                ProjectSerializer(Project.objects.get(id=i)).data["chat_group_id"]
            )
        end_response = []
        for i in response:
            end_response.append(GroupSerializer(Group.objects.get(grp_id=i)).data)
        return JsonResponse(end_response, safe=False)


class __get__group__chat__users__(APIView):
    def get(self, request, pk):
        user = User.objects.get(id=pk)
        team = Team.objects.filter(members=pk)
        serializer = TeamSerialzier(team, many=True)
        project_groups = []
        for i in serializer.data:
            if i["project"] not in project_groups:
                project_groups.append(i["project"])
        response = []
        for i in project_groups:
            response.append(
                str(ProjectSerializer(Project.objects.get(id=i)).data["chat_group_id"])
            )
        end_response = []
        user_group_chats = Group.objects.filter(grp_members=user)
        serializer = GroupSerializer(user_group_chats, many=True)
        print(response)
        for i in serializer.data:
            if i["grp_id"] not in response:
                end_response.append(i)
        return JsonResponse(end_response, safe=False)


class __get__project__recommendations__(APIView):
    def post(self, request):
        user = User.objects.get(id=request.data["id"])
        is_talent = Talent.objects.filter(user=user).exists()
        talent_instance = Talent.objects.get(user=user)
        if is_talent:
            skill = []
            for i in talent_instance.skills:
                skill.append(i)
            print(skill)
            project_ids = project_recomendation(skill)
            response = []
            # for i in project_ids:
            #     project = Project.objects.get(id=i)
            #     serializer = ProjectSerializer(project)
            #     response.append(serializer.data)
            print(project_ids)
            return JsonResponse(project_ids, safe=False)
        else:
            return Response({"error": "You are not a talent"})
