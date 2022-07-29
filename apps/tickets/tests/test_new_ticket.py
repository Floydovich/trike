from django.test import TestCase
from django.urls import reverse

from apps.tickets.models import Ticket


class NewTicketTest(TestCase):
    """
    Return the new_ticket template
    Display ticket types on GET
    Redirects to home page after POST

    Save the ticket type on POST
    """

    url_name = 'new-ticket'

    def test_renders_correct_template(self):
        response = self.client.get(reverse(self.url_name))

        # IMPORTANT: don't change the order of arguments in assertTemplateUsed.
        # It only works when response is the first.
        self.assertTemplateUsed(response, 'new_ticket.html')

    def test_display_ticket_types_on_GET(self):
        response = self.client.get(reverse(self.url_name))

        self.assertIn(Ticket.Kind.BUG, response.content.decode())
        self.assertIn(Ticket.Kind.FEATURE, response.content.decode())

    def test_redirect_to_home_page_after_POST(self):
        # TODO: Move data to setup
        response = self.client.post(reverse(self.url_name), data={
            'kind': 'Bug',
            'ticket_title': 'Title for a new ticket',
            'ticket_description': 'Description for a new ticket',
        })

        self.assertEqual(302, response.status_code)
        self.assertEqual('/', response['location'])

    def test_can_save_a_POST_request(self):
        self.client.post(reverse(self.url_name), data={
            'kind': 'Bug',
            'ticket_title': 'Title for a new ticket',
            'ticket_description': 'Description for a new ticket',
        })

        self.assertEqual(1, Ticket.objects.count())
        new_ticket = Ticket.objects.first()
        self.assertEqual('Title for a new ticket', new_ticket.title)
