from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.base_page import BasePage


class DisappearingElementsPage(BasePage):
    __url = "https://the-internet.herokuapp.com/disappearing_elements"
    __page_header = (By.TAG_NAME, "h3")
    __description_text = (By.XPATH, "//p[contains(., 'This example demonstrates when elements')]")
    
    # Navigation links that may appear/disappear
    __home_link = (By.XPATH, "//a[@href='/' and text()='Home']")
    __about_link = (By.XPATH, "//a[@href='/about/' and text()='About']")
    __contact_us_link = (By.XPATH, "//a[@href='/contact-us/' and text()='Contact Us']")
    __portfolio_link = (By.XPATH, "//a[@href='/portfolio/' and text()='Portfolio']")
    __gallery_link = (By.XPATH, "//a[@href='/gallery/' and text()='Gallery']")
    
    # All navigation links
    __all_nav_links = (By.XPATH, "//ul/li/a")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super().open_url(self.__url)

    @property
    def current_url(self) -> str:
        return super()._driver.current_url

    def disappearing_elements_page_loaded_successfully(self):
        assert super().is_displayed(self.__page_header), "The header is not displayed"

    def is_home_link_displayed(self) -> bool:
        return super().is_displayed(self.__home_link)

    def is_about_link_displayed(self) -> bool:
        return super().is_displayed(self.__about_link)

    def is_contact_us_link_displayed(self) -> bool:
        return super().is_displayed(self.__contact_us_link)

    def is_portfolio_link_displayed(self) -> bool:
        return super().is_displayed(self.__portfolio_link)

    def is_gallery_link_displayed(self) -> bool:
        return super().is_displayed(self.__gallery_link)

    def click_home_link(self):
        if self.is_home_link_displayed():
            super()._click(self.__home_link)

    def click_about_link(self):
        if self.is_about_link_displayed():
            super()._click(self.__about_link)

    def click_contact_us_link(self):
        if self.is_contact_us_link_displayed():
            super()._click(self.__contact_us_link)

    def click_portfolio_link(self):
        if self.is_portfolio_link_displayed():
            super()._click(self.__portfolio_link)

    def click_gallery_link(self):
        if self.is_gallery_link_displayed():
            super()._click(self.__gallery_link)

    def get_all_navigation_links(self):
        return super()._driver.find_elements(*self.__all_nav_links)

    def get_visible_link_count(self) -> int:
        return len(self.get_all_navigation_links())

    def get_visible_link_texts(self) -> list:
        links = self.get_all_navigation_links()
        return [link.text for link in links]