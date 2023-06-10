import time
import pytest

from ui import locators
from ui.test_ui.base import BaseCase

@pytest.mark.UI
class Test1(BaseCase):
    @pytest.mark.UI
    @allure.feature('Ввод текста')
    def test_login(self):
        self.page.enter_text()
        with allure.step("Сравниваем что ввели и что показывает"):
            assert self.page.find(locators.MainPageLocators.P_BLOCK_LOCATOR).text == "ЦГАТ02ГП230ПЕ"
        #time.sleep(1500)
        #assert True

