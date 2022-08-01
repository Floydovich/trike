from behave import *
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select

from apps.tickets.models import Ticket
from features.steps.helpers import *


# Moving from the home page

@when("I go the new ticket form")
def step_impl(context):
    element = context.browser.find_element(By.ID, 'id_new_ticket')
    element.click()


@then("the ticket form is opened")
def step_impl(context):
    context.test.assertEqual(f'{context.base_url}/new-ticket',
                             context.browser.current_url)


# Submitting a new ticket

@given("the ticket form is opened")
def step_impl(context):
    context.browser.get(f'{context.base_url}/new-ticket', )


@when("I select the kind {kind}")
def step_impl(context, kind):
    select = Select(context.browser.find_element(By.ID, 'id_select'))
    select.select_by_visible_text(kind)


@when("I enter the title {title}")
def step_impl(context, title):
    title_inputbox = context.browser.find_element(By.NAME, 'title')
    title_inputbox.send_keys(title)


@step("I submit the ticket")
def step_impl(context):
    button = context.browser.find_element(By.NAME, 'Submit')
    button.send_keys(Keys.ENTER)
    time.sleep(1)


@then("the ticket list on home page is opened")
def step_impl(context):
    context.test.assertEqual(context.base_url + '/', context.browser.current_url)


@step("the list displays the kind {kind}")
def step_impl(context, kind):
    wait_for_cell_in_tickets_table(context, kind)


@then("the list displays the title {title}")
def step_impl(context, title):
    wait_for_cell_in_tickets_table(context, title)


# Scenario: Adding one more ticket

@given("there are tickets submitted earlier")
def step_impl(context):
    context.earlier_tickets = []
    for row in context.table:
        ticket = Ticket.objects.create(
            kind=row['kind'],
            title=row['title'],
        )
        context.earlier_tickets.append(ticket)


@then("the earlier tickets are still in the list")
def step_impl(context):
    for ticket in context.earlier_tickets:
        wait_for_cell_in_tickets_table(context, ticket.title)
