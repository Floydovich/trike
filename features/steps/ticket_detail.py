from behave import *
from selenium.webdriver.common.by import By

from apps.tickets.models import Ticket


@given("the {kind} ticket with {title} and {description} is createad")
def step_impl(context, kind, title, description):
    context.ticket = Ticket.objects.create(
        kind=kind,
        title=title,
        description=description,
    )


@then("the page contains the kind {kind}")
def step_impl(context, kind):
    element = context.browser.find_element(By.ID, 'id_kind')
    context.test.assertEqual(kind, element.text)


@then("the page contains the title {title}")
def step_impl(context, title):
    element = context.browser.find_element(By.ID, 'id_title')
    context.test.assertEqual(title, element.text)


@then("the page contains the description {description}")
def step_impl(context, description):
    element = context.browser.find_element(By.ID, 'id_description')
    context.test.assertEqual(description, element.text)
