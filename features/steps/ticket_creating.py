from behave import *

from apps.tickets.models import Ticket
from features.steps.helpers import *

use_step_matcher("re")


@given("the home page is opened")
def step_impl(context):
    context.browser.get(context.base_url)


@when('I write the ticket title "Cannot create a ticket"')
def step_impl(context):
    pass


@when("I add some text to the ticket description and submit")
def step_impl(context):
    add_title_description_and_submit(
        context,
        'Cannot create a ticket',
        """
        There is no way to create a bug report ticket. The app is
        still very raw and has no basic functionality at all.
        """
    )


@then('the first ticket in the list says "Cannot create a ticket"')
def step_impl(context):
    wait_for_row_in_tickets_table(context, 'Cannot create a ticket')


@given("the home page has one submitted ticket")
def step_impl(context):
    context.browser.get(context.base_url)

    Ticket.objects.create(
        title='Cannot create a ticket',
        description="""
        There is no way to create a bug report ticket. The app is
        still very raw and has no basic functionality at all.
        """
    )


@when("I submit a new ticket with title and description")
def step_impl(context):
    add_title_description_and_submit(
        context,
        'List shows only one ticket',
        """
        When I create more than one ticket the page doesn't show all tickets. It
        Only shows the first one.
        """
    )


@then("the second ticket title is shown on the page")
def step_impl(context):
    wait_for_row_in_tickets_table(context, 'List shows only one ticket')


@then("the first ticket is still there")
def step_impl(context):
    wait_for_row_in_tickets_table(context, 'Cannot create a ticket')
