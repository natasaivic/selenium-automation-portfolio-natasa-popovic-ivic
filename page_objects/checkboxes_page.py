from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.base_page import BasePage


class CheckboxesPage(BasePage):
    __url = "https://the-internet.herokuapp.com/checkboxes"
    __page_header = (By.TAG_NAME, "h3")
    __form = (By.ID, "checkboxes")
    __checkbox_1 = (By.XPATH, "//form[@id='checkboxes']/input[1]")
    __checkbox_2 = (By.XPATH, "//form[@id='checkboxes']/input[2]")
    __all_checkboxes = (By.XPATH, "//form[@id='checkboxes']/input[@type='checkbox']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super().open_url(self.__url)

    def checkboxes_page_loaded_successfully(self):
        assert super().is_displayed(self.__page_header), "The header is not displayed"

    def click_checkbox_1(self):
        super()._click(self.__checkbox_1)

    def click_checkbox_2(self):
        super()._click(self.__checkbox_2)

    def is_checkbox_1_checked(self) -> bool:
        return super()._find(self.__checkbox_1).is_selected()

    def is_checkbox_2_checked(self) -> bool:
        return super()._find(self.__checkbox_2).is_selected()

    def get_all_checkboxes(self):
        return super()._driver.find_elements(*self.__all_checkboxes)

    def get_checkbox_count(self) -> int:
        return len(self.get_all_checkboxes())

    def check_checkbox_1(self):
        if not self.is_checkbox_1_checked():
            self.click_checkbox_1()

    def uncheck_checkbox_1(self):
        if self.is_checkbox_1_checked():
            self.click_checkbox_1()

    def check_checkbox_2(self):
        if not self.is_checkbox_2_checked():
            self.click_checkbox_2()

    def uncheck_checkbox_2(self):
        if self.is_checkbox_2_checked():
            self.click_checkbox_2()