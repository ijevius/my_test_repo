import time
import pytest
import allure

from ui import locators
from ui.test_ui.base import BaseCase

class Test1(BaseCase):
    @pytest.mark.UI
    @allure.feature('Enter text')
    def test_login(self):
        self.page.enter_text()
        with allure.step("Pass text and check"):
            assert self.page.find(locators.MainPageLocators.P_BLOCK_LOCATOR).text == "ЦГАТ02ГП230ПЕ"
        #time.sleep(1500)
        #assert True
    @allure.feature('Second test')
    def test_second(self):
        assert 2*2==4
    @allure.feature('Third test')
    def test_third(self):
        with allure.step("2+2*2"):
            assert 2+2*2==6
    @allure.feature('Fourth test')
    def test_fourth(self):
        with allure.step("Fourth"):
            assert True
    @allure.feature('Fail test')
    def test_shouldfail(self):
        with allure.step("Lets fail"):
            assert 2==3
     
     

