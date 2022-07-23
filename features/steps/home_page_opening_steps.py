from behave import *
from selenium import webdriver

use_step_matcher("re")


@given("the browser is opened")
def step_impl(context):
    context.browser = webdriver.Firefox()

    context.browser.get('http://localhost:8000')

    assert 'Django' in context.browser.page_source


@when("the user moves to the home page")
def step_impl(context):
    raise NotImplementedError(u'STEP: When the user moves to the home page')


@then('there is "Issues" heading on the page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the page has "Welcome to Trike" text')


@step('browser has "trike" in the title')
def step_impl(context):
    raise NotImplementedError(u'STEP: And "trike" in the title')