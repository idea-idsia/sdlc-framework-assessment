## backend/tickets/models.py

from django.db import models
from users.models import User
from datetime import datetime  # Import datetime

class Ticket(models.Model):
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('closed', 'Closed')
    ]

    CATEGORY_CHOICES = [
        ('bug', 'Bug'),
        ('feature_request', 'Feature Request'),
        ('question', 'Question')
    ]

    reporter: User = models.ForeignKey(User, related_name='reported_tickets', on_delete=models.CASCADE)
    status: str = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
    category: str = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    description: str = models.TextField()
    created_at: datetime = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    ticket: Ticket = models.ForeignKey(Ticket, related_name='messages', on_delete=models.CASCADE)
    sender: User = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    content: str = models.TextField()
    timestamp: datetime = models.DateTimeField(auto_now_add=True)
