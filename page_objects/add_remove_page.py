from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.base_page import BasePage


class AddRemoveElementsPage(BasePage):
    __url = "https://the-internet.herokuapp.com/add_remove_elements/"
    __page_header = (By.TAG_NAME, "h3")
    __add_element_button = (By.XPATH, "//button[text()='Add Element']")
    __elements_container = (By.ID, "elements")
    __delete_buttons = (By.XPATH, "//button[@class='added-manually' and text()='Delete']")
    __first_delete_button = (By.XPATH, "//div[@id='elements']/button[1]")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super().open_url(self.__url)

    def add_remove_elements_page_loaded_successfully(self):
        assert super().is_displayed(self.__page_header), "The header is not displayed"
        assert super().is_displayed(self.__add_element_button), "The add element button is not displayed"

    def click_add_element_button(self):
        super()._click(self.__add_element_button)

    def click_delete_button(self, button_index: int = 0):
        delete_buttons = self.get_all_delete_buttons()
        if button_index < len(delete_buttons):
            delete_buttons[button_index].click()

    def click_first_delete_button(self):
        if self.is_first_delete_button_displayed():
            super()._click(self.__first_delete_button)

    def get_all_delete_buttons(self):
        return self._driver.find_elements(*self.__delete_buttons)

    def get_delete_buttons_count(self) -> int:
        return len(self.get_all_delete_buttons())

    def is_first_delete_button_displayed(self) -> bool:
        return super().is_displayed(self.__first_delete_button)

    def is_elements_container_displayed(self) -> bool:
        return super().is_displayed(self.__elements_container)

    def add_multiple_elements(self, count: int):
        for _ in range(count):
            self.click_add_element_button()

    def remove_all_elements(self):
        while self.get_delete_buttons_count() > 0:
            self.click_first_delete_button()

    def get_page_header_text(self) -> str:
        return super()._find(self.__page_header).text

    def verify_elements_added(self, expected_count: int) -> bool:
        return self.get_delete_buttons_count() == expected_count

    def verify_no_elements_present(self) -> bool:
        return self.get_delete_buttons_count() == 0