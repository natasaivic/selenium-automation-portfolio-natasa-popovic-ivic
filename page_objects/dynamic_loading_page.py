from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.base_page import BasePage


class DynamicLoadingPage(BasePage):
    __url = "https://the-internet.herokuapp.com/dynamic_loading"
    __example1_url = "https://the-internet.herokuapp.com/dynamic_loading/1"
    __example2_url = "https://the-internet.herokuapp.com/dynamic_loading/2"
    __page_header = (By.TAG_NAME, "h3")
    __description_paragraph1 = (By.XPATH, "//p[contains(text(), \"It's common to see an action\")]")
    __description_paragraph2 = (By.XPATH, "//p[contains(text(), 'There are two examples')]")
    __example1_link = (By.XPATH, "//a[@href='/dynamic_loading/1']")
    __example2_link = (By.XPATH, "//a[@href='/dynamic_loading/2']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super().open_url(self.__url)

    def open_example1_directly(self):
        super().open_url(self.__example1_url)

    def open_example2_directly(self):
        super().open_url(self.__example2_url)

    def dynamic_loading_page_loaded_successfully(self):
        assert super().is_displayed(self.__page_header), "The header is not displayed"
        assert super().is_displayed(self.__description_paragraph1), "The first description paragraph is not displayed"
        assert super().is_displayed(self.__description_paragraph2), "The second description paragraph is not displayed"

    def click_example1_link(self):
        super()._click(self.__example1_link)

    def click_example2_link(self):
        super()._click(self.__example2_link)

    def is_example1_link_displayed(self) -> bool:
        return super().is_displayed(self.__example1_link)

    def is_example2_link_displayed(self) -> bool:
        return super().is_displayed(self.__example2_link)

    def get_example1_link_text(self) -> str:
        return super()._find(self.__example1_link).text

    def get_example2_link_text(self) -> str:
        return super()._find(self.__example2_link).text

    def get_example1_link_href(self) -> str:
        return super()._find(self.__example1_link).get_attribute("href")

    def get_example2_link_href(self) -> str:
        return super()._find(self.__example2_link).get_attribute("href")

    def get_page_header_text(self) -> str:
        return super()._find(self.__page_header).text

    def get_description_paragraph1_text(self) -> str:
        return super()._find(self.__description_paragraph1).text

    def get_description_paragraph2_text(self) -> str:
        return super()._find(self.__description_paragraph2).text

    def verify_expected_links_present(self) -> bool:
        """Verify both example links are present and have correct text"""
        expected_example1_text = "Example 1: Element on page that is hidden"
        expected_example2_text = "Example 2: Element rendered after the fact"
        
        return (self.is_example1_link_displayed() and 
                self.is_example2_link_displayed() and
                self.get_example1_link_text() == expected_example1_text and
                self.get_example2_link_text() == expected_example2_text)

    def verify_link_hrefs_correct(self) -> bool:
        """Verify both links have correct href attributes"""
        return ("/dynamic_loading/1" in self.get_example1_link_href() and 
                "/dynamic_loading/2" in self.get_example2_link_href())

    def navigate_to_example1(self):
        """Navigate to Example 1 and verify navigation"""
        self.click_example1_link()
        super()._wait_until_url_contains("dynamic_loading/1")

    def navigate_to_example2(self):
        """Navigate to Example 2 and verify navigation"""
        self.click_example2_link()
        super()._wait_until_url_contains("dynamic_loading/2")

    def verify_page_content_structure(self) -> bool:
        """Verify the page has all expected content elements"""
        expected_header = "Dynamically Loaded Page Elements"
        
        return (self.get_page_header_text() == expected_header and
                "It's common to see an action" in self.get_description_paragraph1_text() and
                "There are two examples" in self.get_description_paragraph2_text() and
                self.verify_expected_links_present())