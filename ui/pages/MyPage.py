
from ui.locators import *
from ui.pages.BasePage import BasePage


class MyPage(BasePage):

    def enter_text(self):
        input = self.find(MainPageLocators.INPUT_BLOCK_LOCATOR, 2)
        btn = self.find(MainPageLocators.CLICK_BUTTON_LOCATOR, 2)
        input.clear()
        input.send_keys("ЦГАТ02ГП230ПЕ")
        self.click(MainPageLocators.CLICK_BUTTON_LOCATOR)
        return self