from django.test import TestCase

from apps.tickets.models import Ticket


class TicketModelTest(TestCase):

    """
    Next status
        Can get next status for the ticket
        For the CLOSED status gets None
    """
    
    def test_can_get_next_status(self):
        ticket = Ticket.objects.create()

        self.assertEqual('IN REVIEW', ticket.next_status)

        ticket.status = Ticket.Status.IN_REVIEW
        ticket.save()

        self.assertEqual('CLOSED', ticket.next_status)

        ticket.status = Ticket.Status.CLOSED
        ticket.save()

        self.assertEqual('PENDING', ticket.next_status)
