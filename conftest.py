import pytest
from playwright.sync_api import sync_playwright

# Fixture to initialize browser and provide page object to tests
@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p: # Start Playwright
        browser = p.chromium.launch(headless=False) # Launch Chromium browser (visible mode)
        context = browser.new_context() # Create a new browser context
        page = context.new_page() # Open a new page/tab
        yield page  # Yield the page to test cases
        browser.close() # Close browser after test execution