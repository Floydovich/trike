from django.test import TestCase

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
