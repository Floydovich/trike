from behave import *

from apps.tickets.models import Ticket


@given("the {kind} ticket with {title} and {description} is createad")
def step_impl(context, kind, title, description):
    context.ticket = Ticket.objects.create(
        kind=kind,
        title=title,
        description=description,
    )


@then("the page contains the title {title}")
def step_impl(context, title):
    context.test.assertIn(title, context.browser.page_source)


@then("the page contains the description {description}")
def step_impl(context, description):
    context.test.assertIn(description, context.browser.page_source)
