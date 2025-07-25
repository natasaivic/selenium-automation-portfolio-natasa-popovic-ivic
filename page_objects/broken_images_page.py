from selenium.webdriver.common.by import By 
from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.base_page import BasePage


class BrokenImagesPage(BasePage):
    __url = "https://the-internet.herokuapp.com/broken_images"
    __page_header = (By.TAG_NAME, "h3")
    __first_image = (By.XPATH, "//img[@src='asdf.jpg']")
    __second_image = (By.XPATH, "//img[@src='hjkl.jpg']")
    __third_image = (By.XPATH, "//img[@src='img/avatar-blank.jpg']")
    __all_images = (By.XPATH, "//div[@class='example']//img")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super().open_url(self.__url)

    @property
    def current_url(self) -> str:
        return super()._driver.current_url

    def broken_images_page_loaded_successfully(self):
        assert super().is_displayed(self.__page_header), "The header is not displayed"

    def get_all_images(self):
        return super()._driver.find_elements(*self.__all_images)

    def is_first_image_displayed(self) -> bool:
        return super().is_displayed(self.__first_image)

    def is_second_image_displayed(self) -> bool:
        return super().is_displayed(self.__second_image)

    def is_third_image_displayed(self) -> bool:
        return super().is_displayed(self.__third_image)

    def get_image_src(self, image_locator: tuple) -> str:
        return super()._find(image_locator).get_attribute("src")