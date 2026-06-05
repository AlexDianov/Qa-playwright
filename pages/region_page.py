from playwright. sync_api import Page, expect



class RegionPage():
    def __init__(self, page: Page):
        self.page = page
        self.select_room = page.locator('[data-qa="hotel-result-choose-room"]')
        self.free_cancel = page.get_by_text('Бесплатная отмена бронирования', exact=True)
        self.free_cancel_on_hotel = page.get_by_text('Бесплатная отмена до').first
        self.corp_tarif = page.get_by_text('Корпоративный тариф')
        self.choose_room_button = page.locator('[data-qa="hotel-result-choose-room"]').nth(1)


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


    def open_hotel_in_new_tab(self):
        with self.page.context.expect_page() as new_hotel_page:
            self.choose_room_button.click()

        self.page = new_hotel_page.value
        self.page.wait_for_load_state()

    def wait_button_and_click(self):
        'Ожидание и нажатие кнопки "В корзину"'
        hotel_current_room_cart = self.page.locator('[data-qa="hotel-current-room-cart"]').first

        expect(
            hotel_current_room_cart,
            "Кнопка 'В корзину' должна отображаться"
        ).to_be_visible(timeout=60000)
        hotel_current_room_cart.click()

    def go_to_cart(self):
        "Переход в корзину"
        hotel_cart = self.page.get_by_text('Корзина', exact=True).first
        hotel_cart.click()


