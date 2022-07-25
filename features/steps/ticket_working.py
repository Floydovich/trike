from behave import *
from selenium.webdriver.common.by import By

from apps.tickets.models import Ticket


@given("the list contains two created tickets")
def step_impl(context):
    for row in context.table:
        Ticket.objects.create(title=row['title'],
                              description=row['description'])

    context.browser.get(context.base_url)


@when("I click on the ticket with the title {title}")
def step_impl(context, title):
    ticket_title = context.browser.find_element(By.LINK_TEXT, title)
    ticket_title.click()


@then("the browser opens the ticket {id} detail page")
def step_impl(context, id):
    context.test.assertIn(f'tickets/{id}', context.browser.current_url)


@then("the page contains the title {title}")
def step_impl(context, title):
    context.test.assertIn(title, context.browser.page_source)


@then("the page contains the description {description}")
def step_impl(context, description):
    context.test.assertIn(description, context.browser.page_source)
