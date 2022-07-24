import time

from selenium.webdriver.common.by import By


def check_for_row_in_tickets_table(context, row_text):
    table = context.browser.find_element(By.ID, 'id_tickets_table')
    rows = table.find_elements(By.TAG_NAME, 'tr')
    context.test.assertIn(row_text, [row.text for row in rows])


def add_title_description_and_submit(context, title, description):
    title_inputbox = context.browser.find_element(By.NAME, 'ticket_title')
    title_inputbox.send_keys(title)

    desc_inputbox = context.browser.find_element(By.NAME, 'ticket_description')
    desc_inputbox.send_keys(description)

    desc_inputbox.submit()
    time.sleep(1)  # couldn't find the heading after submit
