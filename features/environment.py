from selenium import webdriver


# noinspection PyTypeHints
def before_all(context):
    context.browser = webdriver.Firefox()


def after_all(context):
    context.browser.quit()
