from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.base_page import BasePage


class LandingPage(BasePage):
    __url = "https://the-internet.herokuapp.com/"
    __url_ab_page = "abtest"
    __url_add_remove_elements_page = "add_remove_elements"
    __url_broken_images_page = "broken_images"
    __url_challenging_dom_page = "challenging_dom"
    __url_checkboxes_page = "checkboxes"
    __url_context_menu_page = "context_menu"
    __url_digest_authentication_page = "digest_auth"
    __url_disappearing_elements_page = "disappearing_elements"
    __url_drag_and_drop_page = "drag_and_drop"
    __url_dropdown_page = "dropdown"
    __url_dynamic_content = "dynamic_content"
    __url_dynamic_controls = "dynamic_controls"
    __url_dynamic_loading = "dynamic_loading"
    __ab_testing_link = (By.XPATH, "//a[contains(., 'A/B Testing')]")
    __add_remove_link = (By.XPATH, "//a[contains(., 'Add/Remove Elements')]")
    __broken_images_link = (By.XPATH, "//a[contains(., 'Broken Images')]")
    __challenging_dom_link = (By.XPATH, "//a[contains(., 'Challenging DOM')]")
    __checkboxes_link = (By.XPATH, "//a[contains(., 'Checkboxes')]")
    __context_menu_link = (By.XPATH, "//a[contains(., 'Context Menu')]")
    __digest_authentication_link = (By.XPATH, "//a[contains(., 'Digest Authentication')]")
    __disappearing_elements_link = (By.XPATH, "//a[contains(., 'Disappearing Elements')]")
    __drag_and_drop_link = (By.XPATH, "//a[contains(., 'Drag and Drop')]")
    __dropdown_link = (By.XPATH, "//a[contains(., 'Dropdown')]")
    __dynamic_content_link = (By.XPATH, "//a[contains(., 'Dynamic Content')]")
    __dynamic_controls_link = (By.XPATH, "//a[contains(., 'Dynamic Controls')]")
    __dynamic_loading_link = (By.XPATH, "//a[contains(., 'Dynamic Loading')]")
    __home_page_header = (By.XPATH, "//a[contains(., 'Welcome to the-internet')]")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super().open_url(self.__url)

    def click_ab_testing_link(self):
        super()._click(self.__ab_testing_link)
        super()._wait_until_url_contains(self.__url_ab_page)

    def click_add_remove_link(self):
        super()._click(self.__add_remove_link)
        super()._wait_until_url_contains(self.__url_add_remove_elements_page)

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

    def click_digest_authentication(self):
        super()._click(self.__digest_authentication_link)
        super()._wait_until_url_contains(self.__url_digest_authentication_page)

    def click_disappearing_elements_link(self):
        super()._click(self.__disappearing_elements_link)
        super()._wait_until_url_contains(self.__url_disappearing_elements_page)

    def click_drag_and_drop_link(self):
        super()._click(self.__drag_and_drop_link)
        super()._wait_until_url_contains(self.__url_drag_and_drop_page)

    def click_dropdown_link(self):
        super()._click(self.__dropdown_link)
        super()._wait_until_url_contains(self.__url_dropdown_page)

    def click_dynamic_content_link(self):
        super()._click(self.__dynamic_content_link)
        super()._wait_until_url_contains(self.__url_dynamic_content)
    
    def click_dynamic_controls_link(self):
        super()._click(self.__dynamic_controls_link)
        super()._wait_until_url_contains(self.__url_dynamic_controls)

    def click_dynamic_loading_link(self):
        super()._click(self.__dynamic_loading_link)
        super()._wait_until_url_contains(self.__url_dynamic_loading)