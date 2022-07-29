from django.test import TestCase
from django.urls import reverse

from apps.tickets.models import Ticket


class NewTicketTest(TestCase):
    """
    Return the new_ticket template
    Display ticket types on GET

    Save the ticket type on POST
    """

    url_name = 'new-ticket'

    def test_renders_correct_template(self):
        response = self.client.get(reverse(self.url_name))

        # IMPORTANT: don't change the order of arguments in assertTemplateUsed.
        # It only works when response is the first.
        self.assertTemplateUsed(response, 'new_ticket.html')

    def test_display_ticket_types_on_GET(self):
        response = self.client.get(reverse('new-ticket'))

        self.assertIn(Ticket.Type.BUG, response.content.decode())
        self.assertIn(Ticket.Type.FEATURE, response.content.decode())
