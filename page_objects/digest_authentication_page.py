from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.base_page import BasePage


class DigestAuthenticationPage(BasePage):
    __url = "https://the-internet.herokuapp.com/digest_auth"
    __page_header = (By.TAG_NAME, "h3")
    __success_message = (By.TAG_NAME, "p")
    __error_message = (By.XPATH, "//h1[contains(text(), \"This page isn't working\")]")
    __http_error_text = (By.XPATH, "//*[contains(text(), 'HTTP ERROR 401')]")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super().open_url(self.__url)

    def open_with_credentials(self, username: str, password: str):
        url_with_auth = f"https://{username}:{password}@the-internet.herokuapp.com/digest_auth"
        super().open_url(url_with_auth)

    def digest_auth_page_loaded_successfully(self):
        assert super().is_displayed(self.__page_header), "The header is not displayed"

    def is_authenticated_successfully(self) -> bool:
        try:
            return (super().is_displayed(self.__success_message) and 
                   "Congratulations! You must have the proper credentials." in self.get_success_message())
        except:
            return False

    def is_authentication_failed(self) -> bool:
        try:
            return (super().is_displayed(self.__error_message) or 
                   super().is_displayed(self.__http_error_text) or
                   "This page isn't working" in self._driver.page_source or
                   "HTTP ERROR 401" in self._driver.page_source)
        except:
            return False

    def get_page_header(self) -> str:
        if super().is_displayed(self.__page_header):
            return super()._find(self.__page_header).text
        return ""

    def get_success_message(self) -> str:
        if super().is_displayed(self.__success_message):
            return super()._find(self.__success_message).text
        return ""

    def get_error_message(self) -> str:
        if super().is_displayed(self.__error_message):
            return super()._find(self.__error_message).text
        return ""

    def is_unauthorized_error_displayed(self) -> bool:
        return self.is_authentication_failed()