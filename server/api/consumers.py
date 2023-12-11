# myapp/consumers.py

"""
This module contains the implementation of a WebSocket consumer for handling chat functionality.

The ChatConsumer class is responsible for handling WebSocket connections and processing incoming and outgoing messages.
It includes methods for connecting to a WebSocket, receiving JSON data, sending messages to users or groups, creating groups, removing users from groups, and more.

"""

import os
import json
from datetime import datetime

from asgiref.sync import sync_to_async
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from django.contrib.auth.models import User
from dotenv import load_dotenv

from .helpers import *
from .llm.message_handler import MessageHandler
from .models import ChatMsg, Group, GroupMessage

load_dotenv()

messages = {}
connectedUsers = {}  # list of all connected users , their id along with their socket_id
handler = MessageHandler(os.environ.get("OPENAI_API_KEY"))

print(connectedUsers)


class ChatConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        print(self.channel_name)
        self.test = []
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        connectedUsers[int(self.room_name)] = self.channel_name
        print(connectedUsers)
        self.room_group_name = f"chat_{self.room_name}"
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def receive_json(self, text_data):
        data = text_data["data"]
        print(data)
        if text_data["type"] == "send_message_to_user":
            await self.send_message_to_user(
                data["message"],
                data["sender"],
                data["receiver"],
                data["group"],
                data["ai"],
            )
        elif text_data["type"] == "create_group":
            await self.create_group(data["group_name"], data["users"], data["admin"])
        elif text_data["type"] == "remove":
            # delete user from the group
            await self.remove_user_from_group(data["group_id"], data["receiver"])
        elif text_data["type"] == "add_user_to_group":
            await self.add_user_to_group(data["group_id"], data["users"])
        elif text_data["type"] == "leave_group":
            await self.leave_user(data["group_id"], data["sender"])

    @database_sync_to_async
    def delete_user_from_group(self, group, user):
        return group.grp_members.remove(user)

    async def leave_user(self, group_id, user_id):
        user = await self.get_user(user_id)
        group = await self.get_group(group_id)
        deleted_group = await self.delete_user_from_group(group, user)
        if user.id in list(connectedUsers.keys()):
            await self.send_json_to_user(
                connectedUsers[user.id],
                {"type": "user_left_group", "group_id": group_id},
            )

    @database_sync_to_async
    def save_user_to_group(self, group, user):
        return group.grp_members.add(user)

    async def add_user_to_group(self, group_id, users):
        group = await self.get_group(group_id)
        for user in users:
            user = await self.get_user(user)
            await self.save_user_to_group(group, user)
        await self.send_json_to_user(self.channel_name, {"type": "user_added_to_group"})
        for user in users:
            if user in list(connectedUsers.keys()):
                await self.send_json_to_user(
                    connectedUsers[user],
                    {"type": "user_added_to_group", "group_id": group_id},
                )

    @database_sync_to_async
    def delete_user_from_group(self, group, user):
        return group.grp_members.remove(user)

    async def remove_user_from_group(self, group_id, user_id):
        user = await self.get_user(user_id)
        group = await self.get_group(group_id)
        deleted_group = await self.delete_user_from_group(group, user)
        await self.send_json_to_user(
            self.channel_name, {"type": "user_removed_from_group"}
        )
        if user in list(connectedUsers.keys()):
            await self.send_json_to_user(
                connectedUsers[user.id],
                {"type": "user_removed_from_group", "group_id": group_id},
            )

    async def create_group(self, group_name, users, admin):
        admin = await self.get_user(admin)
        group = await self.save_group(group_name, admin, users)
        await database_sync_to_async(group.save)()
        # save users to manyTomany Field
        print(users)
        for user in users:
            # send message to each users active
            active_user = await self.get_user(user)
            if active_user.id in list(connectedUsers.keys()):
                await self.send_json_to_user(
                    connectedUsers[active_user.id],
                    {
                        "type": "group_created",
                        "group_name": group_name,
                        "group_id": str(group.grp_id),
                        "admin": str(admin.username),
                    },
                )

    @database_sync_to_async
    def save_group(self, group_name, admin, users):
        # i have a ,many to many field of multiple users linked to a single group and users is an list
        group = Group.objects.create(grp_name=group_name, grp_admin=admin)
        for user in users:
            user = User.objects.get(id=user)
            group.grp_members.add(user)
        group.grp_members.add(admin)
        # save the admin into many To many field
        return group

    @database_sync_to_async
    def get_user(self, id):
        return User.objects.get(id=id)

    @database_sync_to_async
    def save_message(self, message, sender, receiver, date, time, ai):
        return ChatMsg.objects.create(
            message=message,
            sender=sender,
            receiver=receiver,
            created_at_date=date,
            created_at_time=time,
            ai=ai,
        )

    async def send_message_to_user(self, message, sender, receiver, group, ai):
        if group == True:
            await self.send_group_message(message, sender, receiver, ai)
        else:
            await self.send_individual_message(message, sender, receiver, ai)

    @database_sync_to_async
    def get_group(self, id):
        return Group.objects.get(grp_id=id)

    @database_sync_to_async
    def save_group_message(self, message, sender, receiver, date, time, ai):
        return GroupMessage.objects.create(
            message=message,
            sender=sender,
            group=receiver,
            created_at_date=date,
            created_at_time=time,
            ai=ai,
        )

    @database_sync_to_async
    def save_group_instance(self, message):
        return message.save()

    @sync_to_async
    def get_group_users(self, group):
        return list(group.grp_members.all())

    async def send_group_message(self, message, sender, receiver, ai):
        date = getdate()
        time = gettime()
        print("is AI", ai)
        sender = await self.get_user(sender)
        receiver = await self.get_group(receiver)
        message = await self.save_group_message(
            message, sender, receiver, date, time, ai
        )
        await self.save_group_instance(message)
        users = await self.get_group_users(receiver)
        print(users)
        for user in users:
            print(user.id, list(connectedUsers.keys()))
            if user.id in list(connectedUsers.keys()):
                await self.send_json_to_user(
                    connectedUsers[user.id],
                    {
                        "type": "receive_message",
                        "message": message.message,
                        "sender": str(sender.username),
                        "receiver": str(receiver.grp_id),
                        "created_at_date": date,
                        "created_at_time": time,
                        "id": str(message.id),
                        "ai": ai,
                    },
                )

        if ai:
            AI_sender = await self.get_user(4)
            date = getdate()
            time = gettime()
            answer = handler.handle_message(message.message)
            answer_instance = await self.save_group_message(
                answer, AI_sender, receiver, date, time, ai
            )
            await self.save_group_instance(answer_instance)
            for user in users:
                print(user.id, list(connectedUsers.keys()))
                if user.id in list(connectedUsers.keys()):
                    await self.send_json_to_user(
                        connectedUsers[user.id],
                        {
                            "type": "receive_message",
                            "message": answer,
                            "sender": str(AI_sender.username),
                            "receiver": str(receiver.grp_id),
                            "created_at_date": date,
                            "created_at_time": time,
                            "id": str(message.id),
                            "ai": ai,
                        },
                    )

    @database_sync_to_async
    def save_ai_message(self, object1):
        return object1.save()

    async def send_individual_message(self, message, sender, receiver, ai):
        date = getdate()
        time = gettime()
        sender = await self.get_user(sender)
        receiver = await self.get_user(receiver)
        query = await self.save_message(message, sender, receiver, date, time, ai)
        print(message)
        if ai:
            await self.send_json_to_user(
                self.channel_name,
                {
                    "type": "sent_message",
                    "message": message,
                    "sender": str(sender.username),
                    "receiver": str(receiver.username),
                    "created_at_date": date,
                    "created_at_time": time,
                    "id": str(query.id),
                    "ai": ai,
                },
            )
            date = getdate()
            time = gettime()
            answer = handler.handle_message(message)
            save_answer = await self.save_message(
                answer, receiver, sender, date, time, ai
            )
            await self.send_json_to_user(
                self.channel_name,
                {
                    "type": "sent_message",
                    "message": answer,
                    "sender": str(receiver.username),
                    "receiver": str(sender.username),
                    "created_at_date": date,
                    "created_at_time": time,
                    "id": str(query.id),
                    "ai": ai,
                },
            )

        else:
            if receiver.id in list(connectedUsers.keys()):
                await self.send_json_to_user(
                    connectedUsers[receiver.id],
                    {
                        "type": "receive_message",
                        "message": message,
                        "sender": str(sender.username),
                        "receiver": str(receiver.username),
                        "created_at_date": date,
                        "created_at_time": time,
                        "id": str(query.id),
                        "ai": ai,
                    },
                )
            # send message to yourself
            await self.send_json_to_user(
                self.channel_name,
                {
                    "type": "sent_message",
                    "message": message,
                    "sender": str(sender.username),
                    "receiver": str(receiver.username),
                    "created_at_date": date,
                    "created_at_time": time,
                    "id": str(query.id),
                    "ai": ai,
                },
            )

    async def send_json_to_room(self, room_id, data):
        await self.channel_layer.group_send(
            room_id, {"type": "send_json", "data": data}
        )

    async def send_json_to_user(self, socket_id, data):
        await self.channel_layer.send(socket_id, {"type": "send_json", "data": data})

    async def send_json(self, event):
        data = event["data"]
        await self.send(text_data=json.dumps(data))
