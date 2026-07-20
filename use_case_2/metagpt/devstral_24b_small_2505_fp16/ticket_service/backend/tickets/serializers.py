## backend/tickets/serializers.py

from rest_framework import serializers
from .models import Ticket, Message
from users.models import User

class TicketSerializer(serializers.ModelSerializer):
    reporter = serializers.StringRelatedField()
    messages = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Ticket
        fields = ['id', 'reporter', 'status', 'category', 'description', 'created_at', 'messages']
        extra_kwargs = {
            'status': {'default': 'open'},
            'category': {'required': True},
            'description': {'required': True}
        }

class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.StringRelatedField()
    ticket = serializers.PrimaryKeyRelatedField(queryset=Ticket.objects.all())

    class Meta:
        model = Message
        fields = ['id', 'ticket', 'sender', 'content', 'timestamp']
        extra_kwargs = {
            'content': {'required': True}
        }
