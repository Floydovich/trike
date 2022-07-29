import time

from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@given("the new ticket page is opened")
def step_impl(context):
    context.browser.get(f'{context.base_url}/new-ticket')


@when("I select to create a {ticket_type}")
def step_impl(context, ticket_type):
    select = Select(context.browser.find_element(By.ID, 'id_select'))
    select.select_by_visible_text(ticket_type)
    time.sleep(1)


@then("the ticket detail page is opened")
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the ticket detail page is opened')


@step("the ticket type is {ticket_type}")
def step_impl(context, ticket_type):
    raise NotImplementedError(u'STEP: And the ticket type is <type>')