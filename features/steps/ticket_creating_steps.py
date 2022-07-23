from behave import *
from selenium.webdriver.common.by import By

use_step_matcher("re")


@given("the home page is opened")
def step_impl(context):
    context.browser.get('http://localhost:8000')


@when('I write the ticket title "Cannot create a ticket"')
def step_impl(context):
    title_input = context.browser.find_element(By.NAME, '')
    title_input.send_keys('Cannot create a ticket')


@when("I add some text to the ticket description and submit")
def step_impl(context):
    description_input = context.browser.find_element(By.NAME, 'description')
    description_input.send_keys(
        """
        There is no way to create a bug report ticket. The app is
        still very raw and has no basic functionality at all.
        """
    )
    description_input.submit()


@then('the page heading now says "Reported bugs: 1"')
def step_impl(context):
    heading = context.browser.find_element(By.TAG_NAME, 'h1')

    context.test.assertEquals('Reported bugs: 1', heading.text)


@step('the first ticket in the list has title "Cannot create a ticket"')
def step_impl(context):
    table = context.browser.find_element(By.ID, 'id_tickets_table')
    rows = table.find_elements(By.TAG_NAME, 'tr')

    context.test.assertTrue(
        any(row.text == 'Cannot create a ticket' for row in rows)
    )
