from django.test import LiveServerTestCase
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By


class HomePageMobileLayoutTest(LiveServerTestCase):

    RESOLUTION = (412, 915)
    DEFAULT_MARGIN = 12

    def setUp(self):
        self.browser = Firefox()
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(self.RESOLUTION[0], self.RESOLUTION[1])

    def test_new_ticket_button_is_in_the_upper_left_corner(self):
        button = self.browser.find_element(By.ID, 'id_new_ticket')

        self.assertAlmostEqual(button.location['x'], 0,
                               delta=self.DEFAULT_MARGIN + 10)
        self.assertAlmostEqual(button.location['y'], 0,
                               delta=self.DEFAULT_MARGIN + 10)

    def test_heading_is_at_the_center(self):
        heading = self.browser.find_element(By.ID, 'id_heading')

        self.assertAlmostEqual(
            heading.location['x'] + heading.size['width'] // 2,
            self.RESOLUTION[0] // 2,
            delta=self.DEFAULT_MARGIN + 10,
        )

    def tearDown(self):
        self.browser.close()