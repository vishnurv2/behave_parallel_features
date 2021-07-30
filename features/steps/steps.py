"""
Selenium steps to configure behave test scenarios
"""
import time

@when('visit url "{url}"')
def step(context, url):
    context.browser.maximize_window()
    context.browser.get(url)


@when('check if title is "{title}"')
def step(context, title):
    assert context.browser.title == title
