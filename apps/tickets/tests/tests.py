from django.test import TestCase
from django.urls import reverse

from apps.tickets.models import Ticket


class HomePage(TestCase):

    def test_home_page_returns_correct_template(self):
        response = self.client.get('/')

        # IMPORTANT: don't change the order of arguments in assertTemplateUsed.
        # It only works when response is the first.
        self.assertTemplateUsed(response, 'home.html')

    def test_displays_ticket_info(self):
        tickets = [
            {
                'title': 'title 1',
                'kind': 'Bug',
            },
            {
                'title': 'title 2',
                'kind': 'Feature',
            },
        ]

        for ticket in tickets:
            Ticket.objects.create(
                title=ticket['title'],
                kind=ticket['kind'],
            )

        response = self.client.get('/')

        for ticket in tickets:
            for value in ticket.values():
                self.assertIn(value, response.content.decode())


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

    def test_diplays_ticket_kind(self):
        response = self.client.get(
            reverse('ticket_detail', args=[self.ticket.id])
        )

        self.assertIn(self.ticket.kind, response.content.decode())

    def test_can_set_status_on_POST(self):
        self.ticket.status = Ticket.Status.IN_REVIEW
        self.ticket.save()
        expected_status = 'DONE'

        response = self.client.post(
            reverse('ticket_status', args=[self.ticket.id]),
            data={'status': expected_status}
        )
        print(response.status_code)

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
            data={'status': 'DONE'}
        )

        self.assertEqual(302, response.status_code)
        self.assertEqual(f'/tickets/{self.ticket.id}', response['location'])


class TicketModelTest(TestCase):

    def test_saving_and_retrieving_tickets(self):
        first_ticket = Ticket()
        first_ticket.title = 'Ticket 1 title'
        first_ticket.description = 'Ticket 1 description'
        first_ticket.save()

        second_ticket = Ticket()
        second_ticket.title = 'Ticket 2 title'
        second_ticket.description = 'Ticket 2 description'
        second_ticket.save()

        saved_tickets = Ticket.objects.all()
        self.assertEqual(saved_tickets.count(), 2)

        self.assertEqual(saved_tickets[0].title, 'Ticket 1 title')
        self.assertEqual(saved_tickets[1].title, 'Ticket 2 title')
