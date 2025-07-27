from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.base_page import BasePage


class DynamicContentPage(BasePage):
    __url = "https://the-internet.herokuapp.com/dynamic_content"
    __url_static = "https://the-internet.herokuapp.com/dynamic_content?with_content=static"
    __page_header = (By.TAG_NAME, "h3")
    __description_text = (By.XPATH, "//p[contains(text(), 'This example demonstrates')]")
    __static_content_link = (By.XPATH, "//a[@href='/dynamic_content?with_content=static']")
    __content_container = (By.XPATH, "//div[@class='large-10 columns large-centered']")
    __content_rows = (By.XPATH, "//div[@class='large-10 columns large-centered']/div[@class='row']")
    __all_images = (By.XPATH, "//div[@class='large-2 columns']/img")
    __all_text_content = (By.XPATH, "//div[@class='large-10 columns' and not(contains(@class, 'large-centered'))]")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super().open_url(self.__url)

    def open_static_content(self):
        super().open_url(self.__url_static)

    def dynamic_content_page_loaded_successfully(self):
        assert super().is_displayed(self.__page_header), "The header is not displayed"
        assert super().is_displayed(self.__description_text), "The description text is not displayed"

    def click_static_content_link(self):
        super()._click(self.__static_content_link)

    def get_all_content_rows(self):
        return self._driver.find_elements(*self.__content_rows)

    def get_content_rows_count(self) -> int:
        return len(self.get_all_content_rows())

    def get_all_images(self):
        return self._driver.find_elements(*self.__all_images)

    def get_all_text_content(self):
        return self._driver.find_elements(*self.__all_text_content)

    def get_image_sources(self) -> list:
        images = self.get_all_images()
        return [img.get_attribute("src") for img in images]

    def get_text_contents(self) -> list:
        text_elements = self.get_all_text_content()
        return [element.text for element in text_elements]

    def get_content_snapshot(self) -> dict:
        return {
            "images": self.get_image_sources(),
            "texts": self.get_text_contents(),
            "rows_count": self.get_content_rows_count()
        }

    def refresh_page(self):
        self._driver.refresh()

    def compare_content_snapshots(self, snapshot1: dict, snapshot2: dict) -> dict:
        return {
            "images_changed": snapshot1["images"] != snapshot2["images"],
            "texts_changed": snapshot1["texts"] != snapshot2["texts"],
            "rows_count_same": snapshot1["rows_count"] == snapshot2["rows_count"]
        }

    def verify_content_is_dynamic(self) -> bool:
        # Take initial snapshot
        initial_snapshot = self.get_content_snapshot()
        
        # Refresh page
        self.refresh_page()
        self.dynamic_content_page_loaded_successfully()
        
        # Take second snapshot
        refreshed_snapshot = self.get_content_snapshot()
        
        # Compare snapshots
        comparison = self.compare_content_snapshots(initial_snapshot, refreshed_snapshot)
        
        # Content is dynamic if images or texts changed
        return comparison["images_changed"] or comparison["texts_changed"]

    def get_page_header_text(self) -> str:
        return super()._find(self.__page_header).text

    def get_description_text(self) -> str:
        return super()._find(self.__description_text).text

    def is_static_content_link_displayed(self) -> bool:
        return super().is_displayed(self.__static_content_link)

    def get_static_content_link_text(self) -> str:
        return super()._find(self.__static_content_link).text

    def verify_expected_content_structure(self) -> bool:
        # Verify we have exactly 3 content rows
        return self.get_content_rows_count() == 3