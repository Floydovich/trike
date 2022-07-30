from django.test import TestCase
from django.urls import reverse

from apps.tickets.models import Ticket


class TicketDetailsTest(TestCase):
    """
    Returns ticket_detail template
    Displays ticket and description in content
    Displays status in content
    Can set status in POST
        If invalid status doesn't save and return error
    Redirects to detail page
    """

    def setUp(self):
        self.ticket = Ticket.objects.create(
            title='Ticket title',
            description='Ticket description',
            kind='Bug'
        )

    def test_returns_correct_template(self):
        response = self.client.get(
            reverse('ticket_detail', args=[self.ticket.id])
        )

        self.assertTemplateUsed(response, 'ticket_detail.html')

    def test_displays_title_and_description(self):
        response = self.client.get(
            reverse('ticket_detail', args=[self.ticket.id])
        )

        self.assertIn(self.ticket.title, response.content.decode())
        self.assertIn(self.ticket.description, response.content.decode())

    def test_displays_status(self):
        response = self.client.get(
            reverse('ticket_detail', args=[self.ticket.id])
        )

        self.assertIn(self.ticket.status, response.content.decode())

    def test_displays_next_status(self):
        # TODO: Refactor to avoid duplication
        next_status = self.ticket.next_status

        response = self.client.get(
            reverse('ticket_detail', args=[self.ticket.id])
        )

        self.assertEqual('IN REVIEW', next_status)
        self.assertIn(next_status, response.content.decode())

        self.ticket.status = Ticket.Status.IN_REVIEW
        self.ticket.save()
        next_status = self.ticket.next_status

        response = self.client.get(
            reverse('ticket_detail', args=[self.ticket.id])
        )

        self.assertEqual('CLOSED', next_status)
        self.assertIn(next_status, response.content.decode())

        self.ticket.status = Ticket.Status.CLOSED
        self.ticket.save()
        next_status = self.ticket.next_status

        response = self.client.get(
            reverse('ticket_detail', args=[self.ticket.id])
        )

        self.assertEqual('PENDING', next_status)
        self.assertIn(next_status, response.content.decode())

    def test_can_set_status_on_POST(self):
        expected_status = 'IN REVIEW'

        response = self.client.post(
            reverse('ticket_status', args=[self.ticket.id]),
            data={'status': expected_status}
        )

        self.ticket.refresh_from_db()
        self.assertEqual(expected_status, self.ticket.status)

    def test_invalid_status_returns_404_on_POST(self):
        expected_status = self.ticket.status

        response = self.client.post(
            reverse('ticket_status', args=[self.ticket.id]),
            data={'status': 'INVALID'}
        )

        self.ticket.refresh_from_db()
        self.assertEqual(expected_status, self.ticket.status)
        self.assertEqual(404, response.status_code)

    def test_redirect_to_detail_after_status_POST(self):
        response = self.client.post(
            reverse('ticket_status', args=[self.ticket.id]),
            data={'status': 'CLOSED'}
        )

        self.assertEqual(302, response.status_code)
        self.assertEqual(f'/tickets/{self.ticket.id}', response['location'])
