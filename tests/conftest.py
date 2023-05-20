import pytest
from selene import browser, by, be, have


@pytest.fixture()
def browser_start():
    browser.config.window_width = 1520
    browser.config.window_height = 1080

    yield

    browser.quit()