from playwright.sync_api import Page, expect
from pages.start_page import start_page


class SmartdeskPage(start_page):
    def __init__(self, page):
        self.page = page
        self.start_search_title = page.get_by_text("Начните поиск")
        self.hotel_search_button = page.locator('[data-qa="smartdesk-search-panel-searchHotel"]')

    def check_start_search_success(self):
        expect(
            self.start_search_title,
            "Авторизация успешна"
        ).to_be_visible()

    def check_login_failed(self):
        expect(
            self.page.get_by_text("Неверный логин или пароль"),
            "ошибка авторизации"
        ).to_be_visible()

    def select_hotel_service(self):
        """Переход на страницу поиска"""
        self.hotel_search_button.click()
