from django.test import TestCase

from apps.tickets.models import Ticket


class HomePage(TestCase):

    def test_home_page_returns_correct_template(self):
        response = self.client.get('/')

        # IMPORTANT: don't change the order of arguments in assertTemplateUsed.
        # It only works when response is the first.
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_a_POST_request(self):
        self.client.post('/', data={
            'ticket_title': 'Title for a new ticket',
            'ticket_description': 'Description for a new ticket',
        })

        self.assertEqual(1, Ticket.objects.count())
        new_ticket = Ticket.objects.first()
        self.assertEqual('Title for a new ticket', new_ticket.title)

    def test_redirects_after_POST(self):
        response = self.client.post('/', data={
            'ticket_title': 'Title for a new ticket',
            'ticket_description': 'Description for a new ticket',
        })

        self.assertEqual(302, response.status_code)
        self.assertEqual('/', response['location'])

    def test_only_saves_tickets_when_necessary(self):
        self.client.get('/')

        self.assertEqual(0, Ticket.objects.count())

    def test_displays_all_saved_tickets(self):
        Ticket.objects.create(title='title 1', description='description 1')
        Ticket.objects.create(title='title 2', description='description 2')

        response = self.client.get('/')

        self.assertIn('title 1', response.content.decode())
        self.assertIn('title 2', response.content.decode())


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
