from django.test import TestCase
from django.urls import resolve

from apps.tickets.views import home_page


class HomePage(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')

        self.assertEqual(found.func, home_page)
