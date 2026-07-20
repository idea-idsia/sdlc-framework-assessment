## backend/tickets/views.py

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Ticket, Message
from .serializers import TicketSerializer, MessageSerializer
from django.shortcuts import get_object_or_404

@api_view(['GET'])
def get_all_tickets(request):
    """
    Retrieve all tickets.
    """
    tickets = Ticket.objects.all()
    serializer = TicketSerializer(tickets, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_ticket(request):
    """
    Create a new ticket.
    """
    if not request.user.is_authenticated:
        return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)

    data = request.data
    serializer = TicketSerializer(data=data)
    if serializer.is_valid():
        serializer.save(reporter=request.user)  # Assuming user is authenticated and available in the request context
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_ticket(request, ticket_id):
    """
    Update an existing ticket.
    """
    if not request.user.is_authenticated:
        return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)

    ticket = get_object_or_404(Ticket, id=ticket_id)
    data = request.data
    serializer = TicketSerializer(ticket, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_ticket(request, ticket_id):
    """
    Delete a ticket.
    """
    if not request.user.is_authenticated:
        return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)

    ticket = get_object_or_404(Ticket, id=ticket_id)
    ticket.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
