from behave import *


@given("the new ticket page is opened")
def step_impl(context):
    context.browser.get(f'{context.browser.current_url}/new-ticket')


@when("I select to create a {ticket_type}")
def step_impl(context, ticket_type):
    raise NotImplementedError(u'STEP: When I select to create a <type>')


@then("the ticket detail page is opened")
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the ticket detail page is opened')


@step("the ticket type is {ticket_type}")
def step_impl(context, ticket_type):
    raise NotImplementedError(u'STEP: And the ticket type is <type>')