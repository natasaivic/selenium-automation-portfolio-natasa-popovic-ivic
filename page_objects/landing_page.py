from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.base_page import BasePage


class LandingPage(BasePage):
    __url = "https://the-internet.herokuapp.com/"
    __url_ab_page = "abtest"
    __url_broken_images_page = "broken_images"
    __url_challenging_dom_page = "challenging_dom"
    __url_checkboxes_page = "checkboxes"
    __url_context_menu_page = "context_menu"
    __url_disappearing_elements_page = "disappearing_elements"
    __ab_testing_link = (By.XPATH, "//a[contains(., 'A/B Testing')]")
    __add_remove_link = (By.XPATH, "//a[contains(., 'Add/Remove Elements')]")
    __broken_images_link = (By.XPATH, "//a[contains(., 'Broken Images')]")
    __challenging_dom_link = (By.XPATH, "//a[contains(., 'Challenging DOM')]")
    __checkboxes_link = (By.XPATH, "//a[contains(., 'Checkboxes')]")
    __context_menu_link = (By.XPATH, "//a[contains(., 'Context Menu')]")
    __disappearing_elements_link = (By.XPATH, "//a[contains(., 'Disappearing Elements')]")
    __home_page_header = (By.XPATH, "//a[contains(., 'Welcome to the-internet')]")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super().open_url(self.__url)

    def click_ab_testing_link(self):
        super()._click(self.__ab_testing_link)
        super()._wait_until_url_contains(self.__url_ab_page)

    def click_add_remove_link(self):
        super()._click(self.__ab_testing_link)
        super()._wait_until_element_is_not_visible(self.__home_page_header)

    def click_broken_images_link(self):
        super()._click(self.__broken_images_link)
        super()._wait_until_url_contains(self.__url_broken_images_page)

    def click_challenging_dom_link(self):
        super()._click(self.__challenging_dom_link)
        super()._wait_until_url_contains(self.__url_challenging_dom_page)

    def click_checkboxes_link(self):
        super()._click(self.__checkboxes_link)
        super()._wait_until_url_contains(self.__url_checkboxes_page)

    def click_context_menu_link(self):
        super()._click(self.__context_menu_link)
        super()._wait_until_url_contains(self.__url_context_menu_page)

    def click_disappearing_elements_link(self):
        super()._click(self.__disappearing_elements_link)
        super()._wait_until_url_contains(self.__url_disappearing_elements_page)