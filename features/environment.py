from selenium import webdriver


from apps.tickets.models import Ticket


def before_all(context):
    context.browser = webdriver.Firefox()


def after_all(context):
    context.browser.quit()
