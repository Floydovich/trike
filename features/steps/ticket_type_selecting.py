import time

from behave import *
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@given("the new ticket page is opened")
def step_impl(context):
    context.browser.get(f'{context.base_url}/new-ticket')


@when("I select the ticket kind {kind}")
def step_impl(context, kind):
    select = Select(context.browser.find_element(By.ID, 'id_select'))
    select.select_by_visible_text(kind)


@step("I submit the ticket")
def step_impl(context):
    button = context.browser.find_element(By.NAME, 'Submit')
    button.send_keys(Keys.ENTER)
    time.sleep(0.5)


@then("the home page is opened")
def step_impl(context):
    context.test.assertEqual(context.base_url + '/', context.browser.current_url)


@step("the ticket kind is {kind}")
def step_impl(context, kind):
    kinds = context.browser.find_elements(By.ID, 'id_kind')

    context.test.assertIn(kind, [kind.text for kind in kinds])
