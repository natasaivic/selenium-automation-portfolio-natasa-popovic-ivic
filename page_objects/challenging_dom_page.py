from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.base_page import BasePage


class ChallengingDomPage(BasePage):
    __url = "https://the-internet.herokuapp.com/challenging_dom"
    __page_header = (By.TAG_NAME, "h3")
    __description_text = (By.XPATH, "//p[contains(., 'The hardest part in automated web testing')]")
    
    # Buttons with challenging IDs - using class-based locators instead
    __blue_button = (By.XPATH, "//a[@class='button' and text()='foo']")
    __red_button = (By.XPATH, "//a[@class='button alert' and text()='foo']")
    __green_button = (By.XPATH, "//a[@class='button success' and text()='baz']")
    
    # Table elements
    __table = (By.TAG_NAME, "table")
    __table_headers = (By.XPATH, "//table/thead/tr/th")
    __table_rows = (By.XPATH, "//table/tbody/tr")
    __edit_links = (By.XPATH, "//a[@href='#edit']")
    __delete_links = (By.XPATH, "//a[@href='#delete']")
    
    # Canvas element
    __canvas = (By.ID, "canvas")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super().open_url(self.__url)

    @property
    def current_url(self) -> str:
        return super()._driver.current_url

    def challenging_dom_page_loaded_successfully(self):
        assert super().is_displayed(self.__page_header), "The header is not displayed"

    def click_blue_button(self):
        super()._click(self.__blue_button)

    def click_red_button(self):
        super()._click(self.__red_button)

    def click_green_button(self):
        super()._click(self.__green_button)

    def get_table_row_count(self) -> int:
        return len(super()._driver.find_elements(*self.__table_rows))

    def get_table_headers(self):
        return super()._driver.find_elements(*self.__table_headers)

    def click_edit_link_by_row(self, row_index: int):
        edit_links = super()._driver.find_elements(*self.__edit_links)
        if row_index < len(edit_links):
            edit_links[row_index].click()

    def click_delete_link_by_row(self, row_index: int):
        delete_links = super()._driver.find_elements(*self.__delete_links)
        if row_index < len(delete_links):
            delete_links[row_index].click()

    def get_table_cell_text(self, row_index: int, column_index: int) -> str:
        cell_locator = (By.XPATH, f"//table/tbody/tr[{row_index + 1}]/td[{column_index + 1}]")
        return super()._find(cell_locator).text

    def is_canvas_displayed(self) -> bool:
        return super().is_displayed(self.__canvas)

    def get_canvas_element(self):
        return super()._find(self.__canvas)