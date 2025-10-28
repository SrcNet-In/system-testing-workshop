import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from playwright.sync_api import Page

scenarios('../ui_test_demo/test_site_capabilities_ui.feature')

@given(parsers.parse('the user navigates to "{url}"'))
def navigate_to_page(page: Page, url: str):
    """Navigate to the given documentation URL."""
    pass

@when("the page is loaded")
def wait_for_page_load(page: Page):
    """Wait for DOM content to be loaded completely."""
    #use page.wait_for_load_state("domcontentloaded")
    pass

@then(parsers.parse('the page title should be "{expected_title}"'))
def verify_page_title(page: Page, expected_title: str):
    """Verify that the page title matches the expected value."""
    #title exists in page.title()
    pass
