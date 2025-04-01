import pytest

@pytest.fixture()
def setup(playwright):
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    try:
        yield page
    finally:
        browser.close()