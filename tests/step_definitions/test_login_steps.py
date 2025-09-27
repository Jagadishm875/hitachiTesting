import pytest
from pytest_bdd import scenario, given, when, then
from playwright.sync_api import sync_playwright

@scenario("../features/login.feature", "Successful login")
def test_login():
    pass


@given("I open the login page")
def open_login_page():
    global page, browser, playwright
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://magento.softwaretestingboard.com/customer/account/login/")

@when("I enter valid credentials")
def enter_credentials():
    page.fill("#email", "test@example.com")     # use your test email
    page.fill("#pass", "Password123")           # use your test passwosrd
    page.click("button.login")

@then("I should see the dashboard")
def verify_dashboard():
    assert "My Account" in page.title()
    browser.close()
    playwright.stop()
