from django.test import TestCase

from apps.tickets.models import Ticket


class HomePageTest(TestCase):

    def test_home_page_returns_correct_template(self):
        response = self.client.get('/', )

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

        response = self.client.get('/', )

        for ticket in tickets:
            for value in ticket.values():
                self.assertIn(value, response.content.decode())
