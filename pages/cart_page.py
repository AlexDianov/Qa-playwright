from playwright.sync_api import Page, expect


class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.cart_price_item = page.locator('[data-qa="cart-price-item"]')

    def check_hotel_in_cart(self):

        expect(
            self.cart_price_item.first, "Проверка нахождения рейта в корзине"
        ).to_be_visible()
