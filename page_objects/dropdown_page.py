from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import Select

from page_objects.base_page import BasePage


class DropdownPage(BasePage):
    __url = "https://the-internet.herokuapp.com/dropdown"
    __page_header = (By.TAG_NAME, "h3")
    __dropdown = (By.ID, "dropdown")
    __option_1 = (By.XPATH, "//option[@value='1']")
    __option_2 = (By.XPATH, "//option[@value='2']")
    __default_option = (By.XPATH, "//option[@value='' and @disabled='disabled']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super().open_url(self.__url)

    def dropdown_page_loaded_successfully(self):
        assert super().is_displayed(self.__page_header), "The header is not displayed"
        assert super().is_displayed(self.__dropdown), "The dropdown is not displayed"

    def get_dropdown_element(self):
        return super()._find(self.__dropdown)

    def get_select_object(self):
        return Select(self.get_dropdown_element())

    def select_option_by_value(self, value: str):
        select = self.get_select_object()
        select.select_by_value(value)

    def select_option_by_text(self, text: str):
        select = self.get_select_object()
        select.select_by_visible_text(text)

    def select_option_by_index(self, index: int):
        select = self.get_select_object()
        select.select_by_index(index)

    def select_option_1(self):
        self.select_option_by_value("1")

    def select_option_2(self):
        self.select_option_by_value("2")

    def get_selected_option_text(self) -> str:
        select = self.get_select_object()
        return select.first_selected_option.text

    def get_selected_option_value(self) -> str:
        select = self.get_select_object()
        return select.first_selected_option.get_attribute("value")

    def get_all_options(self):
        select = self.get_select_object()
        return select.options

    def get_all_option_texts(self) -> list:
        options = self.get_all_options()
        return [option.text for option in options]

    def get_all_option_values(self) -> list:
        options = self.get_all_options()
        return [option.get_attribute("value") for option in options]

    def is_option_1_selected(self) -> bool:
        return self.get_selected_option_value() == "1"

    def is_option_2_selected(self) -> bool:
        return self.get_selected_option_value() == "2"

    def is_default_option_selected(self) -> bool:
        return self.get_selected_option_text() == "Please select an option"

    def get_options_count(self) -> int:
        return len(self.get_all_options())

    def verify_dropdown_has_expected_options(self) -> bool:
        expected_texts = ["Please select an option", "Option 1", "Option 2"]
        actual_texts = self.get_all_option_texts()
        return actual_texts == expected_texts

    def get_page_header_text(self) -> str:
        return super()._find(self.__page_header).text