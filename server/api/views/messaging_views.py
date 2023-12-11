from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from ..models.chat import *
from ..serializers import *


class __get__group__messages__(APIView):
    def post(self, request):
        """
        Retrieve the messages of a group.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            JsonResponse: The JSON response containing the group messages.

        Raises:
            Response: If the user is not a member of the group.
        """
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
        """
        Retrieve the messages of a personal chat.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            JsonResponse: The JSON response containing the personal chat messages.
        """
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
        """
        Retrieve the AI messages of a user.

        Args:
            request (HttpRequest): The HTTP request object.
            pk (int): The primary key of the user.

        Returns:
            Response: The response containing the AI messages.
        """
        # Get user chats related to the user and return the messages of that user if ai = True
        user = request.user
        receiver = User.objects.get(id=pk)
        messages = ChatMsg.objects.filter(sender=user, receiver=user, ai=True)
        serializer = ChatMsgSerializer(messages, many=True)
        return Response(serializer.data)
    

class __get__users__recent__chat__(APIView):
    def get(self, request):
        """
        Retrieve the recent private/group chat of a user.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            JsonResponse: The JSON response containing the recent chat messages.
        """
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


class __get__direct__chat__users__(APIView):
    def get(self, request, pk):
        """
        Retrieve the users involved in direct chats with a user.

        Args:
            request (HttpRequest): The HTTP request object.
            pk (int): The primary key of the user.

        Returns:
            JsonResponse: The JSON response containing the direct chat users.
        """
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
    
class __get__group__chat__users__(APIView):
    def get(self, request, pk):
        """
        Retrieve the users involved in group chats with a user.

        Args:
            request (HttpRequest): The HTTP request object.
            pk (int): The primary key of the user.

        Returns:
            JsonResponse: The JSON response containing the group chat users.
        """
        user = User.objects.get(id=pk)
        team = Team.objects.filter(members=pk)
        serializer = TeamSerializer(team, many=True)
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
    

class __get__project__related__groups__(APIView):
    def get(self, request, pk):
        """
        Retrieve the groups related to a project.

        Args:
            request (HttpRequest): The HTTP request object.
            pk (int): The primary key of the user.

        Returns:
            JsonResponse: The JSON response containing the project-related groups.
        """
        user = User.objects.get(id=pk)
        team = Team.objects.filter(members=pk)
        serializer = TeamSerializer(team, many=True)
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
