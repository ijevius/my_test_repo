import pytest
from _pytest.fixtures import FixtureRequest
from selenium.common.exceptions import StaleElementReferenceException

CLICK_RETRY = 3

class BaseCase:
    driver = None
    config = None

    def click(self, locator):
        for i in range(CLICK_RETRY):
            try:
                element = self.find(locator)
                if i < 2:
                    self.driver.refresh()
                element.click()
                return
            except StaleElementReferenceException:
                if i == CLICK_RETRY - 1:
                    raise

    def find(self, locator):
        return self.driver.find_element(*locator)

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.page = request.getfixturevalue('mypage')
        self.config = config