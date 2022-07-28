from behave import *
from selenium.webdriver import Keys

from apps.tickets.models import Ticket
from features.steps.helpers import *


@given("the home page is opened")
def step_impl(context):
    context.browser.get(context.base_url)


@when("I enter the title {title}")
def step_impl(context, title):
    title_inputbox = context.browser.find_element(By.NAME, 'ticket_title')
    title_inputbox.send_keys(title)


@step("I enter the description")
def step_impl(context):
    desc_inputbox = context.browser.find_element(By.NAME, 'ticket_description')
    desc_inputbox.send_keys(context.text)


@step("I press the submit button")
def step_impl(context):
    button = context.browser.find_element(By.NAME, 'Submit')
    button.send_keys(Keys.ENTER)


@then("{title} is displayed in the list")
def step_impl(context, title):
    wait_for_row_in_tickets_table(context, title)


@given("the page has submitted ticket")
def step_impl(context):
    context.browser.get(context.base_url)
    context.old_ticket = Ticket.objects.create(
        title='previous ticket', description='some description'
    )


@then("the previously created ticket is still in the list")
def step_impl(context):
    wait_for_row_in_tickets_table(context, context.old_ticket.title)
