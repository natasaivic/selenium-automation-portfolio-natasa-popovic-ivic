from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains

from page_objects.base_page import BasePage


class DragAndDropPage(BasePage):
    __url = "https://the-internet.herokuapp.com/drag_and_drop"
    __page_header = (By.TAG_NAME, "h3")
    __columns_container = (By.ID, "columns")
    __column_a = (By.ID, "column-a")
    __column_b = (By.ID, "column-b")
    __column_a_header = (By.XPATH, "//div[@id='column-a']/header")
    __column_b_header = (By.XPATH, "//div[@id='column-b']/header")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super().open_url(self.__url)

    def drag_and_drop_page_loaded_successfully(self):
        assert super().is_displayed(self.__page_header), "The header is not displayed"
        assert super().is_displayed(self.__columns_container), "The columns container is not displayed"

    def get_column_a_text(self) -> str:
        return super()._find(self.__column_a_header).text

    def get_column_b_text(self) -> str:
        return super()._find(self.__column_b_header).text

    def drag_column_a_to_column_b(self):
        source_element = super()._find(self.__column_a)
        target_element = super()._find(self.__column_b)
        
        actions = ActionChains(self._driver)
        actions.drag_and_drop(source_element, target_element).perform()

    def drag_column_b_to_column_a(self):
        source_element = super()._find(self.__column_b)
        target_element = super()._find(self.__column_a)
        
        actions = ActionChains(self._driver)
        actions.drag_and_drop(source_element, target_element).perform()

    def is_column_a_displayed(self) -> bool:
        return super().is_displayed(self.__column_a)

    def is_column_b_displayed(self) -> bool:
        return super().is_displayed(self.__column_b)

    def get_columns_initial_state(self) -> dict:
        return {
            "column_a": self.get_column_a_text(),
            "column_b": self.get_column_b_text()
        }

    def verify_columns_swapped(self, initial_state: dict) -> bool:
        current_a = self.get_column_a_text()
        current_b = self.get_column_b_text()
        
        return (current_a == initial_state["column_b"] and 
                current_b == initial_state["column_a"])

    def reset_to_initial_state(self):
        # If columns are swapped (A shows "B" and B shows "A"), swap them back
        if self.get_column_a_text() == "B" and self.get_column_b_text() == "A":
            self.drag_column_a_to_column_b()