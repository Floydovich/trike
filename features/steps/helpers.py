import time

from selenium.common import WebDriverException
from selenium.webdriver.common.by import By

MAX_TIME = 10


def wait_for_cell_in_tickets_table(context, cell_text):
    start_time = time.time()
    while True:
        try:
            table = context.browser.find_element(By.ID, 'id_tickets_table')
            cells = table.find_elements(By.TAG_NAME, 'td')

            context.test.assertIn(cell_text, [cell.text for cell in cells])
            return
        except (AssertionError, WebDriverException) as e:
            if time.time() - start_time > MAX_TIME:
                raise e
            time.sleep(0.5)
