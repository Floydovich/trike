from django.test import TestCase

from apps.tickets.models import Ticket


class HomePage(TestCase):

    def test_home_page_returns_correct_template(self):
        response = self.client.get('/')

        # IMPORTANT: don't change the order of arguments in assert function. It
        # only works when response is the first.
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data={
            'ticket_title': 'Title for a new ticket',
        })

        self.assertIn('Title for a new ticket', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')


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
