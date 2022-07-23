from behave import *
from selenium.webdriver.common.by import By

use_step_matcher("re")


@given("the browser is opened")
def step_impl(context):
    pass


@when("I move to the home page")
def step_impl(context):
    context.browser.get('http://localhost:8000')


@then('the browser title is "trike"')
def step_impl(context):
    context.test.assertEquals('trike', context.browser.title)


@then('there is "Bugs and features" heading on the page')
def step_impl(context):
    heading = context.browser.find_element(By.TAG_NAME, 'h1')

    context.test.assertEquals('Bugs and features', heading)


@given("the home page is opened")
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the home page is opened')


@when("I write the ticket title")
def step_impl(context):
    raise NotImplementedError(u'STEP: When I write the ticket title')


@step("I add some text to the ticket description")
def step_impl(context):
    raise NotImplementedError(u'STEP: And I add some text to the ticket description')


@step("I click the submit button")
def step_impl(context):
    raise NotImplementedError(u'STEP: And I click the submit button')


@then("the browser opens the home page again")
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the browser opens the home page again')


@step("I see the ticket title in the list on page")
def step_impl(context):
    raise NotImplementedError(u'STEP: And I see the ticket title in the list on page')