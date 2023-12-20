''' This module is used for pre and post conditions before execution code '''
# Your test file

# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome
from Lib.Utiles.base_page_object import Basepage  # Corrected import statement
from selenium import webdriver


import pytest

URL = "https://www.facebook.com/"

def pytest_addoption(parser):
    parser.addoption("--browser", action='store')

@pytest.fixture
def cls_browser(request):
    return request.config.getoption("--browser")

@pytest.fixture
def browser_assignment(cls_browser):
    browser = cls_browser

    if browser == 'Chrome':
        browser = Basepage(webdriver.Chrome())
        browser.visit_url(URL)
    else:
        raise Exception("browser {} is not a valid browser".format(browser))

    yield browser

    browser.quit_browser()
