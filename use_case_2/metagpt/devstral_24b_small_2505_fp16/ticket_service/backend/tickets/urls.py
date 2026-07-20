## backend/tickets/urls.py

from django.urls import path
from .views import get_all_tickets, create_ticket, update_ticket, delete_ticket

urlpatterns = [
    path('', get_all_tickets, name='get-all-tickets'),
    path('create/', create_ticket, name='create-ticket'),
    path('<int:ticket_id>/', update_ticket, name='update-ticket'),
    path('<int:ticket_id>/delete/', delete_ticket, name='delete-ticket'),
]
