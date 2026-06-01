from playwright. sync_api import Page, expect
from pages.start_page import start_page
from pages.smartdesk_page import SmartdeskPage
from pages.hotels_search_page import SearchPage


class RegionPage():
    def __init__(self, page: Page):
        self.page = page
        self.select_room = page.locator('[data-qa="hotel-result-choose-room"]')
        self.free_cancel = page.get_by_text('Бесплатная отмена бронирования', exact=True)
        self.free_cancel_on_hotel = page.get_by_text('Бесплатная отмена до')





    def check_select_room_button(self):
        expect(
            self.select_room.first,
            "Появилась кнопка выбора рейта на странице поиска"
        ).to_be_visible(timeout=10000)


    def click_free_cancel(self):
        "Нажатие фильтра Бесплатная отмена"
        self.free_cancel.click()

    def check_free_cancel_on_hotel(self):
        'Проверка выдачи на рейты с бесплатной отменой'
        expect(
            self.free_cancel_on_hotel,
            "Появился рейт с бесплатной отменой на выдаче"
        ).to_be_visible(timeout=10000)

    def check_no_free_cancel_on_hotel(self):
        'Отсутствие рейтов с бесплатной отменой на выдаче'
        expect(
            self.free_cancel_on_hotel,
            "Рейты с бесплатной отменой отсутсвуют в выдаче"
        ).not_to_be_visible()
