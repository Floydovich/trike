from behave import *
from selenium.webdriver.common.by import By

from apps.tickets.models import Ticket
from helpers import wait_for_cell_in_tickets_table


@given("there are two created tickets")
def step_impl(context):
    context.tickets = []
    for row in context.table:
        ticket = Ticket.objects.create(
            kind=row['kind'],
            title=row['title'],
            description=row['description']
        )
        context.tickets.append(ticket)


@given("there is a created ticket")
def step_impl(context):
    context.ticket = Ticket.objects.create(title='A ticket title', kind='Bug')


@step("the home page is opened")
def step_impl(context):
    context.browser.get(context.base_url, )


@when("I select a ticket from the list")
def step_impl(context):
    link = context.browser.find_element(By.TAG_NAME, 'a')
    link.click()


@then("the browser opens the ticket detail")
def step_impl(context):
    expected_url = context.base_url + f'/tickets/{context.ticket.id}'

    context.test.assertEqual(expected_url, context.browser.current_url)


@then("the ticket kinds are in the list")
def step_impl(context):
    for ticket in context.tickets:
        wait_for_cell_in_tickets_table(context, ticket.kind)


@then("the ticket titles are in the list")
def step_impl(context):
    for ticket in context.tickets:
        wait_for_cell_in_tickets_table(context, ticket.title)


@then("the ticket statuses are in the list")
def step_impl(context):
    for ticket in context.tickets:
        wait_for_cell_in_tickets_table(context, ticket.status)
