from behave import *

from apps.tickets.models import Ticket
from helpers import wait_for_cell_in_tickets_table


@given("the list contains two created tickets")
def step_impl(context):
    context.tickets = []
    for row in context.table:
        ticket = Ticket.objects.create(
            kind=row['kind'],
            title=row['title'],
            description=row['description']
        )
        context.tickets.append(ticket)


@when("the home page is opened")
def step_impl(context):
    context.browser.get(context.base_url)


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