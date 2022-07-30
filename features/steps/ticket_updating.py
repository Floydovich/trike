import time

from behave import *
from selenium.webdriver.common.by import By

from apps.tickets.models import Ticket


STATUSES = {
    'PENDING': Ticket.Status.PENDING,
    'IN REVIEW': Ticket.Status.IN_REVIEW,
    'CLOSED': Ticket.Status.DONE,
}


@given("the ticket status is {current_status}")
def step_impl(context, current_status):
    context.ticket = Ticket.objects.create(status = STATUSES[current_status])


@given("the ticket detail page is opened")
def step_impl(context):
    context.detail_page_url = f'{context.base_url}/tickets/{context.ticket.id}'

    context.browser.get(context.detail_page_url)

    context.test.assertEqual(context.detail_page_url, context.browser.current_url)

    statusbox = context.browser.find_element(By.ID, 'id_status')

    context.test.assertEqual(context.ticket.status, statusbox.text)


@when("I mark the ticket as {status}")
def step_impl(context, status):
    status_button = context.browser.find_element(By.ID, 'id_status_switch')
    status_button.click()
    time.sleep(0.5)


@then("the ticket status is changed to {status}")
def step_impl(context, status):
    context.test.assertEqual(context.detail_page_url,context.browser.current_url)

    statusbox = context.browser.find_element(By.ID, 'id_status')
    context.test.assertEqual(status, statusbox.text)