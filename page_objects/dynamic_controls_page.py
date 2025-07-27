from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from page_objects.base_page import BasePage


class DynamicControlsPage(BasePage):
    __url = "https://the-internet.herokuapp.com/dynamic_controls"
    __page_header = (By.TAG_NAME, "h4")
    __description_text = (By.XPATH, "//p[contains(text(), 'This example demonstrates')]")
    
    # Remove/Add section
    __remove_add_subheader = (By.XPATH, "//h4[text()='Remove/add']")
    __checkbox_form = (By.ID, "checkbox-example")
    __checkbox_container = (By.ID, "checkbox")
    __checkbox_input = (By.XPATH, "//input[@type='checkbox']")
    __checkbox_remove_button = (By.XPATH, "//form[@id='checkbox-example']/button")
    
    # Enable/Disable section
    __enable_disable_subheader = (By.XPATH, "//h4[text()='Enable/disable']")
    __input_form = (By.ID, "input-example")
    __text_input = (By.XPATH, "//form[@id='input-example']/input[@type='text']")
    __input_enable_button = (By.XPATH, "//form[@id='input-example']/button")
    
    # Dynamic elements
    __loading_indicator = (By.ID, "loading")
    __message = (By.ID, "message")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super().open_url(self.__url)

    def dynamic_controls_page_loaded_successfully(self):
        assert super().is_displayed(self.__page_header), "The header is not displayed"
        assert super().is_displayed(self.__description_text), "The description text is not displayed"
        assert super().is_displayed(self.__checkbox_form), "The checkbox form is not displayed"
        assert super().is_displayed(self.__input_form), "The input form is not displayed"

    # Checkbox Remove/Add functionality
    def click_checkbox_remove_button(self):
        super()._click(self.__checkbox_remove_button)

    def wait_for_loading_to_disappear(self, timeout: int = 5):
        """Wait for the loading indicator to disappear"""
        wait = WebDriverWait(self._driver, timeout)
        wait.until(ec.invisibility_of_element_located(self.__loading_indicator))

    def wait_for_checkbox_to_be_removed(self, timeout: int = 5):
        """Wait for checkbox to be removed from DOM"""
        wait = WebDriverWait(self._driver, timeout)
        wait.until(ec.invisibility_of_element_located(self.__checkbox_input))

    def wait_for_checkbox_to_be_added(self, timeout: int = 5):
        """Wait for checkbox to be added to DOM"""
        wait = WebDriverWait(self._driver, timeout)
        wait.until(ec.visibility_of_element_located(self.__checkbox_input))

    def is_checkbox_present(self) -> bool:
        return super().is_displayed(self.__checkbox_input)

    def is_checkbox_container_present(self) -> bool:
        return super().is_displayed(self.__checkbox_container)

    def get_checkbox_button_text(self) -> str:
        return super()._find(self.__checkbox_remove_button).text

    def remove_checkbox(self):
        """Complete workflow to remove checkbox with proper waits"""
        if self.is_checkbox_present():
            self.click_checkbox_remove_button()
            self.wait_for_loading_to_disappear()
            self.wait_for_checkbox_to_be_removed()

    def add_checkbox(self):
        """Complete workflow to add checkbox with proper waits"""
        if not self.is_checkbox_present():
            self.click_checkbox_remove_button()
            self.wait_for_loading_to_disappear()
            self.wait_for_checkbox_to_be_added()

    # Input Enable/Disable functionality
    def click_input_enable_button(self):
        super()._click(self.__input_enable_button)

    def get_input_button_text(self) -> str:
        return super()._find(self.__input_enable_button).text

    def is_text_input_enabled(self) -> bool:
        input_element = super()._find(self.__text_input)
        return input_element.is_enabled()

    def is_text_input_disabled(self) -> bool:
        return not self.is_text_input_enabled()

    def wait_for_input_to_be_enabled(self, timeout: int = 5):
        """Wait for input field to be enabled"""
        wait = WebDriverWait(self._driver, timeout)
        wait.until(lambda driver: self.is_text_input_enabled())

    def wait_for_input_to_be_disabled(self, timeout: int = 5):
        """Wait for input field to be disabled"""
        wait = WebDriverWait(self._driver, timeout)
        wait.until(lambda driver: self.is_text_input_disabled())

    def enable_text_input(self):
        """Complete workflow to enable text input with proper waits"""
        if self.is_text_input_disabled():
            self.click_input_enable_button()
            self.wait_for_loading_to_disappear()
            self.wait_for_input_to_be_enabled()

    def disable_text_input(self):
        """Complete workflow to disable text input with proper waits"""
        if self.is_text_input_enabled():
            self.click_input_enable_button()
            self.wait_for_loading_to_disappear()
            self.wait_for_input_to_be_disabled()

    def type_in_text_input(self, text: str):
        """Type text in the input field if it's enabled"""
        if self.is_text_input_enabled():
            super()._type(self.__text_input, text)

    # Message functionality
    def is_message_displayed(self) -> bool:
        return super().is_displayed(self.__message)

    def get_message_text(self) -> str:
        if self.is_message_displayed():
            return super()._find(self.__message).text
        return ""

    def wait_for_message_to_appear(self, timeout: int = 5):
        """Wait for success message to appear"""
        wait = WebDriverWait(self._driver, timeout)
        wait.until(ec.visibility_of_element_located(self.__message))

    # Loading indicator
    def is_loading_displayed(self) -> bool:
        return super().is_displayed(self.__loading_indicator)

    def wait_for_loading_to_appear(self, timeout: int = 2):
        """Wait for loading indicator to appear"""
        wait = WebDriverWait(self._driver, timeout)
        wait.until(ec.visibility_of_element_located(self.__loading_indicator))

    # Utility methods
    def get_page_header_text(self) -> str:
        return super()._find(self.__page_header).text

    def get_description_text(self) -> str:
        return super()._find(self.__description_text).text

    def verify_initial_state(self) -> bool:
        """Verify page is in expected initial state"""
        return (self.is_checkbox_present() and 
                self.get_checkbox_button_text() == "Remove" and
                self.is_text_input_disabled() and 
                self.get_input_button_text() == "Enable")