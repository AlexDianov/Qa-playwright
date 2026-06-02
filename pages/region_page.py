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
        self.corp_tarif = page.get_by_text('Корпоративный тариф')
        self.choose_room_button = page.locator('[data-qa="hotel-result-choose-room"]')
        self.hotel_current_room_cart = page.locator('[data-qa="hotel-current-room-cart"]')
        self.room_wrapper = page.locator(('[data-qa="hotel-current-room-wrapper"]'))





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

    def check_corp_tarif_avaliable(self):
        'Наличие корпоративного тарифа на выдаче'
        expect(
            self.corp_tarif,
            "Корпоративный тариф есть в выдаче"
        ).to_be_visible(timeout=10000)

    def click_to_choose_room_button(self):
        'Нажатие кнопки выбора номера'
        self.choose_room_button.click()

    def wait_room_wrapper(self):
        expect(
            self.room_wrapper,
        'Ожидаем прогрузку рейтов'
        ).to_be_visible(timeout=30000)

    def wait_button(self):
        expect(
            self.hotel_current_room_cart
        ).to_be_visible(timeout=40000)

    def click_hotel_current_room_cart(self):
        'Нажатие кнопки добавления рейта в корзину'
        self.hotel_current_room_cart.click()

