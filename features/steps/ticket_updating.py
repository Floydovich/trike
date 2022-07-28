from behave import *
from selenium.webdriver.common.by import By

from apps.tickets.models import Ticket


@given("the ticket detail page is opened")
def step_impl(context):
    ticket = Ticket.objects.create(title='title', description='description')
    detail_page_url = f'{context.base_url}/tickets/{ticket.id}'

    context.browser.get(detail_page_url)

    context.test.assertEqual(detail_page_url, context.browser.current_url)


@given("the ticket status is {status}")
def step_impl(context, status):
    status_element = context.browser.find_element(By.ID, 'status')
    context.test.assertEqual(status, status_element.text)


@when("I mark the ticket as {status}")
def step_impl(context, status):
    raise NotImplementedError(u'STEP: When I mark the ticket as <status>')


@then("the ticket status is changed to {status}")
def step_impl(context, status):
    raise NotImplementedError(u'STEP: Then the ticket status is changed to <status>')