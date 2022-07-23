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


@then('the page heading says "No reported bugs"')
def step_impl(context):
    heading = context.browser.find_element(By.TAG_NAME, 'h1')

    context.test.assertEquals('No reported bugs', heading.text)