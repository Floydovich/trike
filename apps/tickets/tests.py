from django.test import TestCase

from apps.tickets.views import home_page


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