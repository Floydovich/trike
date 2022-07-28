from django.test import TestCase
from django.urls import reverse


class NewTicketTest(TestCase):
    """
    Returns the new_ticket template
    """

    url_name = 'new-ticket'

    def test_renders_correct_template(self):
        response = self.client.get(reverse(self.url_name))

        # IMPORTANT: don't change the order of arguments in assertTemplateUsed.
        # It only works when response is the first.
        self.assertTemplateUsed(response, 'new_ticket.html')

