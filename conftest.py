import pytest
import ui.locators as locators
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ui.pages.BasePage import BasePage
from ui.pages.MyPage import MyPage

capabilities = {
    "browserName": "chrome",
    "browserVersion": "113.0",
    "selenoid:options": {
        "enableVideo": False,
        "enableVNC": True
    }
}

@pytest.fixture
def base_page(driver):
    return BasePage(driver=driver)

@pytest.fixture
def mypage(driver):
    return MyPage(driver=driver)

def pytest_addoption(parser):
    pass

@pytest.fixture(scope='session')
def config(request):
    return {}

@pytest.fixture(scope='function')
def driver(config):
    browser = webdriver.Remote(
        command_executor="http://192.168.1.39:4444/wd/hub",
        to_capabilities=capabilities)

    browser.maximize_window()

    browser.get('http://192.168.1.61:4567/')

    yield browser
    browser.close()
