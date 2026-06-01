from playwright. sync_api import Page, expect
from pages.start_page import start_page
from pages.smartdesk_page import SmartdeskPage


class SearchPage:
    def __init__(self, page: Page):
        self.page = page
        self.hotel_title = page.get_by_placeholder('Город или гостиница')#locator('[data-qa="hotel-search-title"]')
        self.hotel_search = page.locator('[data-qa="hotel-search-suggest"]')
        self.search_check_in = page.locator('[data-qa="hotel-search-check-in"]')
        self.search_check_out = page.locator('[data-qa="hotel-search-check-out"]')
        self.hotel_search_travelers = page.locator('[data-qa="hotel-search-travelers"]')
        self.early_check_in = page.locator('[data-qa="hotel-search-early-in"]')
        self.late_check_out = page.locator('[data-qa="hotel-search-late-out"]')
        self.search_button = page.locator('[data-qa="hotel-search-button"]')
        self.region_name = page.locator('[data-qa="hotel-search-suggest-result-0"]')

    def search_region_name (self, region):
        """Поиск региона и проверка активности кнопки поиска"""
        self.hotel_search.click()
        self.hotel_search.fill(region)
        self.region_name.wait_for(state="visible")
        self.region_name.click()



    def check_search_button_enabled(self):
        expect(
            self.search_button,
            "Кнопка поиска должна быть активна"
        ).to_be_enabled()

    def check_search_button_disabled(self):
        expect(
            self.search_button,
            "Кнопка поиска должна быть неактивна"
        ).to_be_disabled()

    def click_to_search_button(self):
        """Нажатие кнопки поиска"""
        self.search_button.click()
