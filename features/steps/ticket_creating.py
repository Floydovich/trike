from behave import *
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select

from apps.tickets.models import Ticket
from features.steps.helpers import *


# Scenario: Submitting a new ticket

@given("the new ticket page is opened")
def step_impl(context):
    context.browser.get(f'{context.base_url}/new-ticket')


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


@then("the home page is opened")
def step_impl(context):
    context.test.assertEqual(context.base_url + '/', context.browser.current_url)


@step("the list displays the kind {kind}")
def step_impl(context, kind):
    wait_for_cell_in_tickets_table(context, kind)


@then("the list displays the title {title}")
def step_impl(context, title):
    wait_for_cell_in_tickets_table(context, title)


# Scenario: Adding one more ticket

@given("the page has submitted ticket")
def step_impl(context):
    context.old_ticket = Ticket.objects.create(
        title='previous ticket',
        description='some description',
        kind='Feature'
    )


@then("the previously created ticket is still in the list")
def step_impl(context):
    wait_for_cell_in_tickets_table(context, context.old_ticket.title)
