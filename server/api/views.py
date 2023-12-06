from django.shortcuts import render
from rest_framework.views import APIView
from .models.chat import *
from .models.user import *
from .models.projects import *
from .models.community import *
from .serializers import *
from .utils import *
from .llm import *
from rest_framework.response import Response
from django.http import JsonResponse
from .llm.prd import *
from .llm.workflow import *
# Create your views here.


class __get__group__messages__(APIView):
    def get(self,request,pk):
        # get user , get the group id from pk , query the group messages and return the messages of that group if ai=True
        user = request.user
        group = Group.objects.get(grp_id=pk)
        if user in group.grp_members.all():
            messages = GroupMessage.objects.filter(group=group)
            serializer = GroupMessageSerializer(messages,many=True)
            return Response(serializer.data)
        else:
            return Response({"error":"You are not a member of this group"})
        

class __get__personal__chat__(APIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]
    #ordering in terms of date

    def post(self,request):
        receiver = request.data['receiver']
        sender = request.user
        chats = ChatMsg.objects.filter(sender=sender,receiver=receiver) | ChatMsg.objects.filter(sender=receiver,receiver=sender)
        #order it in terms of date
        chats = chats.order_by('created_at_date','created_at_time')
        serializer = ChatMsgSerializer(chats,many=True)
        #send the user name instead of the id
        response = []
        for i in serializer.data:
            response.append({
                "message":i['message'],
                "sender":UserSerializer(User.objects.get(id=i['sender'])).data,
                "receiver":UserSerializer(User.objects.get(id=i['receiver'])).data,
                "created_at_date":i['created_at_date'],
                "created_at_time":i['created_at_time'],
                "ai":i['ai']
            })
        return JsonResponse(response,safe=False)

class __get__ai__messages__(APIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]
    #ordering in terms of date

    def get(self,request):
        
        sender = request.user
        receiver = 4
        chats = ChatMsg.objects.filter(sender=sender,receiver=receiver,ai=True) | ChatMsg.objects.filter(sender=receiver,receiver=sender,ai=True)
        #order it in terms of date
        chats = chats.order_by('created_at_date','created_at_time')
        serializer = ChatMsgSerializer(chats,many=True)
        #send the user name instead of the id
        response = []
        for i in serializer.data:
            response.append({
                "message":i['message'],
                "sender":UserSerializer(User.objects.get(id=i['sender'])).data,
                "receiver":UserSerializer(User.objects.get(id=i['receiver'])).data,
                "created_at_date":i['created_at_date'],
                "created_at_time":i['created_at_time'],
                "ai":i['ai']
            })
        return JsonResponse(response,safe=False)
    

class __get__user__data__(APIView):
    def get(self,request):
        # get user data
        try:
            user = request.user
            #check if users is a client,talent / mentor and send the data along with the user data
            is_client = Client.objects.filter(user=user).exists()
            is_talent = Talent.objects.filter(user=user).exists()
            is_mentor = Mentor.objects.filter(user=user).exists()
            if is_client:
                client = Client.objects.get(user=user)
                serializer = ClientSerializer(client)
                #also add the user details to the client data
                user_serializer = UserSerializer(user)
                user_data = user_serializer.data
                user_data.update(serializer.data)
                return Response(user_data)
            elif is_talent:
                talent = Talent.objects.get(user=user)
                serializer = TalentSerializer(talent)
                user_serializer = UserSerializer(user)
                user_data = user_serializer.data
                user_data.update(serializer.data)
                return Response(user_data)
            elif is_mentor:
                mentor = Mentor.objects.get(user=user)
                serializer = MentorSerializer(mentor)
                user_serializer = UserSerializer(user)
                user_data = user_serializer.data
                user_data.update(serializer.data)
                return Response(user_data)
            else:
                return Response({"error":"User not found"})
        except:
            return Response({"error":"User not found"})
        
class __get__users__recent__chat__(APIView):
    def get(self,request):
        #get users recent private / group chat
        user = request.user
        #get the recent chat of the user
        recent_chat = ChatMsg.objects.filter(sender=user).order_by('-created_at_date','-created_at_time')
        serializer = ChatMsgSerializer(recent_chat,many=True)
        recent_group_chat = GroupMessage.objects.filter(sender=user).order_by('-created_at_date','-created_at_time')
        group_serializer = GroupMessageSerializer(recent_group_chat,many=True)
        #combine both group and recent chat and order them again
        chat = list(serializer.data) + list(group_serializer.data)
        chat.sort(key=lambda x: (x['created_at_date'],x['created_at_time']),reverse=True)
        return JsonResponse(chat,safe=False)
    
class __create__project__(APIView):
    def post(self,request):
        #create a project
        user = request.user
        #check if user is a client
        is_client = Client.objects.filter(user=user).exists()
        if is_client:
            #get the client
            client = Client.objects.get(user=user)
            #create a project
            project = Project.objects.create(created_by=client,title=request.data['title'],description=request.data['description'],bid_price=request.data['bid_price'],project_doc=request.data['project_doc'],related_techstacks=request.data['related_techstacks'])
            project.save()
        else:
            return Response({"error":"You are not a client"})
        

def __generate__prd__(project_title,project_desc,project_start_date,project_end_date):
    response = {
        "project_overview":None,
        "project_goals":None,
        "original_requirements":None,
        "user_stories":None,
        "system_architecture":None,
        "requirements_analysis":None,
        "ui_ux_design":None,
        "development_methodology":None,
        "security_measures":None,
        "testing_strategy":None,
        "scalability_and_performance":None,
        "deployment_plan":None,
        "maintenance_and_support":None,
        "risks_and_mitigations":None,
        "compliance_and_regulations":None,
        "budget_and_resources":None,
        "timeline_and_milestones":None,
        "communication_plan":None,
        "anything_unclear":None,
        
    }
    '''
    call your llm and make it predict the prd using the above parameters
    return a dictionary of all the parameters in the predicted prd similar to the ProjectRequirementDocument model
    '''
    
    return response

class __send__generated__prd__(APIView):
    def post(self,request):
        #send the generated prd to the client
        user = request.user
        #check if user is a client
        is_client = Client.objects.filter(user=user).exists()
        if is_client:
            #get the client
            client = Client.objects.get(user=user)
            #get the project
            project = Project.objects.get(id=request.data['project_id'])
            #check if the client is the owner of the project
            if project.created_by == client:
                #generate the prd
                prd_id = generate_prd_button_clicked(project)
                prd = ProjectRequirementDocument.objects.get(id=prd_id)
                serializer = ProjectRequirementDocumentSerializer(prd)
                return JsonResponse({"success":"PRD generated successfully","data":serializer.data})
            else:
                return Response({"error":"You are not the owner of this project"})
        else:
            return Response({"error":"You are not a client"})
        

class __get__details__of__project__(APIView):
    def get(self,request,pk):
        #get the details of the project
        user = request.user
        #check if user is a client
        # check if the person accessing it is in the Team and the Team is in the project
        project = Project.objects.get(id=pk)
        team = Team.objects.filter(project=project)
        if team:
            team = team[0]
            if user in team.members.all():
                serializer = ProjectSerializer(project)
                return Response(serializer.data)
            else:
                return Response({"error":"You are not a member of this project"})
        else:
            return Response({"error":"No team found for this project"})
        



class __client__accept__bid__(APIView):
    def post(self,request):
        #accept the bid of the talent
        user = request.user
        data = request.data
        #check if user is a client

        is_client = Client.objects.filter(user=user).exists()
        if is_client:
            #get the client
            client = Client.objects.get(user=user)
            #get the project
            project = Project.objects.get(id=request.data['project_id'])
            #check if the client is the owner of the project
            if project.created_by == client:
                #filter team with the given team id 
                team = Team.objects.get(id=data['team_id'])
                team.project = project
                team.save()
                #get the team members
                team_members = list(team.members.all())
                #create a group
                group = Group.objects.create(grp_name=data['team_name'],grp_admin=client,grp_members=team_members)
                group.save()

                #update the project
                project.chat_group_id = group
                project.save()
            else:
                return Response({"error":"You are not the owner of this project"})
        else:
            return Response({"error":"You are not a client"})
        



class __send__generated__workflow__(APIView):
    def post(self,request):
        #send the generated workflow to the client
        user = request.user
        #check if user is a client
        is_talent = Talent.objects.filter(user=user).exists()
        if is_talent:
            #check if the person is a team leader else dont allow him to send the workflow
            talent = Talent.objects.get(user=user)
            #get the project
            project = Project.objects.get(id=request.data['project_id'])
            #check if the talent is the team leader of the project
            #get the team
            team = Team.objects.filter(project=project)

            if team:
                #check if the user is the teeam leader
                team = team[0]
                if talent == team.team_leader:
                    #generate the workflow
                    workflow = make_workflow(project)
                    return JsonResponse({"success":"Workflow generated successfully","data":workflow})
                else:
                    return Response({"error":"You are not the team leader of this project"})
        else:
            return Response({"error":"You are not a client"})
        

from django.shortcuts import render
from rest_framework.views import APIView
from .models.chat import *
from .models.user import *
from .models.projects import *
from .models.community import *
from .serializers import *
from .utils import *
from .llm import *
from .llm.leaning_resource import learning_resource
from rest_framework.response import Response
from django.http import JsonResponse

# Create your views here.


class __get__group__messages__(APIView):
    def get(self, request, pk):
        # get user , get the group id from pk , query the group messages and return the messages of that group if ai=True
        user = request.user
        group = Group.objects.get(grp_id=pk)
        if user in group.grp_members.all():
            messages = GroupMessage.objects.filter(group=group)
            serializer = GroupMessageSerializer(messages, many=True)
            return Response(serializer.data)
        else:
            return Response({"error": "You are not a member of this group"})


class __get__personal__chat__(APIView):
    def get(self, request, pk):
        # get user chats related to the user and return the messages of that user if ai = False
        user = request.user
        receiver = User.objects.get(id=pk)
        messages = ChatMsg.objects.filter(sender=user, receiver=receiver, ai=False)
        serializer = ChatMsgSerializer(messages, many=True)
        return Response(serializer.data)


class __get__ai__messages__(APIView):
    def __get__ai__messages__(request, pk):
        # get user chats related to the user and return the messages of that user if ai = True
        user = request.user
        receiver = User.objects.get(id=pk)
        messages = ChatMsg.objects.filter(sender=user, receiver=user, ai=True)
        serializer = ChatMsgSerializer(messages, many=True)
        return Response(serializer.data)


class __get__user__data__(APIView):
    def get(self, request):
        # get user data
        try:
            user = request.user
            # check if users is a client,talent / mentor and send the data along with the user data
            is_client = Client.objects.filter(user=user).exists()
            is_talent = Talent.objects.filter(user=user).exists()
            is_mentor = Mentor.objects.filter(user=user).exists()
            if is_client:
                client = Client.objects.get(user=user)
                serializer = ClientSerializer(client)
                # also add the user details to the client data
                user_serializer = UserSerializer(user)
                user_data = user_serializer.data
                user_data.update(serializer.data)
                return Response(user_data)
            elif is_talent:
                talent = Talent.objects.get(user=user)
                serializer = TalentSerializer(talent)
                user_serializer = UserSerializer(user)
                user_data = user_serializer.data
                user_data.update(serializer.data)
                return Response(user_data)
            elif is_mentor:
                mentor = Mentor.objects.get(user=user)
                serializer = MentorSerializer(mentor)
                user_serializer = UserSerializer(user)
                user_data = user_serializer.data
                user_data.update(serializer.data)
                return Response(user_data)
            else:
                return Response({"error": "User not found"})
        except:
            return Response({"error": "User not found"})


class __get__users__recent__chat__(APIView):
    def get(self, request):
        # get users recent private / group chat
        user = request.user
        # get the recent chat of the user
        recent_chat = ChatMsg.objects.filter(sender=user).order_by(
            "-created_at_date", "-created_at_time"
        )
        serializer = ChatMsgSerializer(recent_chat, many=True)
        recent_group_chat = GroupMessage.objects.filter(sender=user).order_by(
            "-created_at_date", "-created_at_time"
        )
        group_serializer = GroupMessageSerializer(recent_group_chat, many=True)
        # combine both group and recent chat and order them again
        chat = list(serializer.data) + list(group_serializer.data)
        chat.sort(
            key=lambda x: (x["created_at_date"], x["created_at_time"]), reverse=True
        )
        return JsonResponse(chat, safe=False)


class __create__project__(APIView):
    def post(self, request):
        # create a project
        user = request.user
        # check if user is a client
        is_client = Client.objects.filter(user=user).exists()
        if is_client:
            # get the client
            client = Client.objects.get(user=user)
            # create a project
            project = Project.objects.create(
                created_by=client,
                title=request.data["title"],
                description=request.data["description"],
                bid_price=request.data["bid_price"],
                project_doc=request.data["project_doc"],
                related_techstacks=request.data["related_techstacks"],
            )
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
        # send the generated prd to the client
        user = request.user
        # check if user is a client
        is_client = Client.objects.filter(user=user).exists()
        if is_client:
            # get the client
            client = Client.objects.get(user=user)
            # get the project
            project = Project.objects.get(id=request.data["project_id"])
            # check if the client is the owner of the project
            if project.created_by == client:
                # generate the prd
                prd = generate_prd_button_clicked(project)
                # prd is a dictionary
                # save the prd in the ProjectRequirementDocument model
                PRD_instance = ProjectRequirementDocument.objects.create(
                    project_overview=prd["project_overview"],
                    project_goals=prd["project_goals"],
                    original_requirements=prd["original_requirements"],
                    user_stories=prd["user_stories"],
                    system_architecture=prd["system_architecture"],
                    requirements_analysis=prd["requirements_analysis"],
                    ui_ux_design=prd["ui_ux_design"],
                    development_methodology=prd["development_methodology"],
                    security_measures=prd["security_measures"],
                    testing_strategy=prd["testing_strategy"],
                    scalability_and_performance=prd["scalability_and_performance"],
                    deployment_plan=prd["deployment_plan"],
                    maintenance_and_support=prd["maintenance_and_support"],
                    risks_and_mitigations=prd["risks_and_mitigations"],
                    compliance_and_regulations=prd["compliance_and_regulations"],
                    budget_and_resources=prd["budget_and_resources"],
                    timeline_and_milestones=prd["timeline_and_milestones"],
                    communication_plan=prd["communication_plan"],
                    anything_unclear=prd["anything_unclear"],
                )
                # save the prd in the project
                PRD_instance.save()
                project.prd = PRD_instance
                project.save()
                return JsonResponse(
                    {"success": "PRD generated successfully", "data": prd}
                )
            else:
                return Response({"error": "You are not the owner of this project"})
        else:
            return Response({"error": "You are not a client"})


class __get__details__of__project__(APIView):
    def get(self, request, pk):
        # get the details of the project
        user = request.user
        # check if user is a client
        # check if the person accessing it is in the Team and the Team is in the project
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
        # accept the bid of the talent
        user = request.user
        data = request.data
        # check if user is a client

        is_client = Client.objects.filter(user=user).exists()
        if is_client:
            # get the client
            client = Client.objects.get(user=user)
            # get the project
            project = Project.objects.get(id=request.data["project_id"])
            # check if the client is the owner of the project
            if project.created_by == client:
                # filter team with the given team id
                team = Team.objects.get(id=data["team_id"])
                team.project = project
                team.save()
                # get the team members
                team_members = list(team.members.all())
                # create a group
                group = Group.objects.create(
                    grp_name=data["team_name"],
                    grp_admin=client,
                    grp_members=team_members,
                )
                group.save()

                # update the project
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
        # send the generated workflow to the client
        user = request.user
        # check if user is a client
        is_talent = Talent.objects.filter(user=user).exists()
        if is_talent:
            # check if the person is a team leader else dont allow him to send the workflow
            talent = Talent.objects.get(user=user)
            # get the project
            project = Project.objects.get(id=request.data["project_id"])
            # check if the talent is the team leader of the project
            # get the team
            team = Team.objects.filter(project=project)

            if team:
                # check if the user is the team leader
                team = team[0]
                if talent == team.team_leader:
                    # generate the workflow
                    workflow = generate_workflow(
                        project.title,
                        project.description,
                        project.timeline,
                        team.members,
                    )
                    # save the workflow in the Workflow model
                    project.workflow = workflow
                    project.save()
                    return JsonResponse(
                        {"success": "Workflow generated successfully", "data": workflow}
                    )
                else:
                    return Response(
                        {"error": "You are not the team leader of this project"}
                    )
        else:
            return Response({"error": "You are not a client"})


class __project__management__(APIView):
    def post(self, request):
        user = request.user
        data = request.data

        is_talent = Talent.objects.filter(user=user).exists()

        if is_talent:
            talent = Talent.objects.filter(user=user)
            project = Project.objects.get(id=data["project_id"])

            team = Team.objects.filter(project=project)
            


class __learning__resource__(APIView):
    def post(self, request):
        user = request.user
        data = request.data

        is_talent = Talent.objects.filter(user=user).exists()

        if is_talent:
            talent = Talent.objects.filter(user=user)
            project = Project.objects.get(id=data["project_id"])

            if team:
                team = team[0]

                learning_resource = learning_resource(talent, project)
                project.learning_resource = learning_resource
                project.save()
                return JsonResponse(
                    {"success": "Management generated successfully", "data": learning_resource}
                )
            else:
                return Response({"error": "Error occured"})
