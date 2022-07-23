from django.test import TestCase


class SmokeTest(TestCase):
    def test_true_is_false(self):
        assert True is False
