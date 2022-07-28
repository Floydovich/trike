import time

from selenium.common import WebDriverException
from selenium.webdriver.common.by import By

MAX_TIME = 10


def wait_for_row_in_tickets_table(context, row_text):
    start_time = time.time()
    while True:
        try:
            table = context.browser.find_element(By.ID, 'id_tickets_table')
            rows = table.find_elements(By.TAG_NAME, 'tr')

            context.test.assertIn(row_text, [row.text for row in rows])
            return
        except (AssertionError, WebDriverException) as e:
            if time.time() - start_time > MAX_TIME:
                raise e
            time.sleep(0.5)
