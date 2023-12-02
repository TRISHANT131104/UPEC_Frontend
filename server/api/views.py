from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.response import Response
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
    def get(self,request,pk):
        # get user chats related to the user and return the messages of that user if ai = False
        user = request.user
        receiver = User.objects.get(id=pk)
        messages = ChatMsg.objects.filter(sender=user,receiver=receiver,ai=False)
        serializer = ChatMsgSerializer(messages,many=True)
        return Response(serializer.data)

class __get__ai__messages__(APIView):
    def __get__ai__messages__(request,pk):
        # get user chats related to the user and return the messages of that user if ai = True
        user = request.user
        receiver = User.objects.get(id=pk)
        messages = ChatMsg.objects.filter(sender=user,receiver=receiver,ai=True)
        serializer = ChatMsgSerializer(messages,many=True)
        return Response(serializer.data)



