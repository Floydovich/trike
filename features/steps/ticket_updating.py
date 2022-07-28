import time

from behave import *
from selenium.webdriver.common.by import By

from apps.tickets.models import Ticket


@given("the ticket detail page is opened")
def step_impl(context):
    ticket = Ticket.objects.create(title='title', description='description')
    context.detail_page_url = f'{context.base_url}/tickets/{ticket.id}'

    context.browser.get(context.detail_page_url)

    context.test.assertEqual(context.detail_page_url, context.browser.current_url)


@given("the ticket status is PENDING")
def step_impl(context):
    statusbox = context.browser.find_element(By.ID, 'status')

    context.test.assertEqual('PENDING', statusbox.text)


@when("I mark the ticket as {status}")
def step_impl(context, status):
    status_button = context.browser.find_element(By.ID, status)
    status_button.click()
    time.sleep(0.5)


@then("the ticket status is changed to {status}")
def step_impl(context, status):
    context.test.assertEqual(context.detail_page_url,context.browser.current_url)

    statusbox = context.browser.find_element(By.ID, 'status')
    context.test.assertEqual(status, statusbox.text)