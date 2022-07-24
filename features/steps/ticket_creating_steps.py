import time

from behave import *
from selenium.webdriver.common.by import By

use_step_matcher("re")


@given("the home page is opened")
def step_impl(context):
    context.browser.get('http://localhost:8000')


@when('I write the ticket title "Cannot create a ticket"')
def step_impl(context):
    title_inputbox = context.browser.find_element(By.NAME, 'ticket_title')
    title_inputbox.send_keys('Cannot create a ticket')


@when("I add some text to the ticket description and submit")
def step_impl(context):
    description_inputbox = context.browser.find_element(By.NAME, 'ticket_description')
    description_inputbox.send_keys(
        """
        There is no way to create a bug report ticket. The app is
        still very raw and has no basic functionality at all.
        """
    )
    description_inputbox.submit()
    time.sleep(1)  # couldn't find the heading after submit


@then('the first ticket in the list says "Cannot create a ticket"')
def step_impl(context):
    table = context.browser.find_element(By.ID, 'id_tickets_table')
    rows = table.find_elements(By.TAG_NAME, 'tr')

    context.test.assertIn('Cannot create a ticket',  [row.text for row in rows])


@then('the page heading now says "Reported bugs: 1"')
def step_impl(context):
    heading = context.browser.find_element(By.TAG_NAME, 'h1')

    context.test.assertEquals('Reported bugs: 1', heading.text)


@given("the home page has one submitted ticket")
def step_impl(context):
    title_inputbox = context.browser.find_element(By.NAME, 'ticket_title')
    title_inputbox.send_keys('Cannot create a ticket')
    description_inputbox = context.browser.find_element(By.NAME, 'ticket_description')
    description_inputbox.send_keys(
        """
        There is no way to create a bug report ticket. The app is
        still very raw and has no basic functionality at all.
        """
    )
    description_inputbox.submit()
    time.sleep(1)  # couldn't find the heading after submit


@when("I submit a new ticket with title and description")
def step_impl(context):
    # TODO: Fixture form sending for reusing
    title_inputbox = context.browser.find_element(By.NAME, 'ticket_title')
    title_inputbox.send_keys('List shows only one ticket')
    description_inputbox = context.browser.find_element(By.NAME, 'ticket_description')
    description_inputbox.send_keys(
        """
        When I create more than one ticket the page doesn't show all tickets. It
        Only shows the first one.
        """
    )
    description_inputbox.submit()
    time.sleep(1)  # couldn't find the heading after submit


@then("the second ticket title is shown on the page")
def step_impl(context):
    table = context.browser.find_element(By.ID, 'id_tickets_table')
    context.rows = table.find_elements(By.TAG_NAME, 'tr')

    context.test.assertIn('List shows only one ticket',  [row.text for row in context.rows])


@then("the first ticket is still there")
def step_impl(context):
    context.test.assertIn('Cannot create a ticket',  [row.text for row in context.rows])


@then('the page heading now says "Reported bugs: 2"')
def step_impl(context):
    heading = context.browser.find_element(By.TAG_NAME, 'h1')

    context.test.assertEquals('Reported bugs: 2', heading.text)
