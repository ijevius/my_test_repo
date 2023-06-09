import pytest
from _pytest.fixtures import FixtureRequest

class BaseCase:
    #driver = None
    #config = None

    '''def click(self, locator):
        for i in range(CLICK_RETRY):
            try:
                element = self.find(locator)
                if i < 2:
                    self.driver.refresh()
                element.click()
                return
            except StaleElementReferenceException:
                if i == CLICK_RETRY - 1:
                    raise'''


    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.page = request.getfixturevalue('mypage')
        self.config = config
