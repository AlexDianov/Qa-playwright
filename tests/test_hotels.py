from pages.cart_page import CartPage

def test_login_success(valid_user, login_page, smartdesk_page):
    """Проверка успешного логина"""
    login_page.navigate_to_login_page()
    login_page.login(valid_user["username"], valid_user["password"])
    smartdesk_page.check_start_search_success()

def test_login_with_invalid_password(invalid_user, login_page):
    """Проверка неуспешного логина"""
    login_page.navigate_to_login_page()
    login_page.login(invalid_user["username"], invalid_user["password"])
    login_page.check_login_failed()

def test_search_button_enables(login_page, smartdesk_page, hotels_search_page, name_region_search,valid_user):
    """Проверка активности кнопки поиска после ввода данных"""
    login_page.navigate_to_login_page()
    login_page.login(valid_user["username"], valid_user["password"])
    smartdesk_page.select_hotel_service()
    hotels_search_page.search_region_name(name_region_search)
    hotels_search_page.check_search_button_enabled()

def test_sucsess_finished_search(login_page, smartdesk_page, hotels_search_page, name_region_search, region_page, valid_user):
    """Проверка отображения выдачи после поиска"""
    login_page.navigate_to_login_page()
    login_page.login(valid_user["username"], valid_user["password"])
    smartdesk_page.select_hotel_service()
    hotels_search_page.search_region_name(name_region_search)
    hotels_search_page.check_search_button_enabled()
    hotels_search_page.click_to_search_button()
    region_page.check_select_room_button()

def test_free_cancel_room(login_page, smartdesk_page, hotels_search_page, name_region_search, region_page, valid_user):
    """Проверка отображения рейтов с бесплатной отменой на выдаче"""
    login_page.navigate_to_login_page()
    login_page.login(valid_user["username"], valid_user["password"])
    smartdesk_page.select_hotel_service()
    hotels_search_page.search_region_name(name_region_search)
    hotels_search_page.check_search_button_enabled()
    hotels_search_page.click_to_search_button()
    region_page.click_free_cancel()
    region_page.check_free_cancel_on_hotel()

def test_corp_tarif_avaliable(login_page, smartdesk_page, hotels_search_page, name_region_search, region_page, valid_user):
    """Проверка наличия корп. тарифа на выдаче"""
    login_page.navigate_to_login_page()
    login_page.login(valid_user["username"], valid_user["password"])
    smartdesk_page.select_hotel_service()
    hotels_search_page.search_region_name(name_region_search)
    hotels_search_page.check_search_button_enabled()
    hotels_search_page.click_to_search_button()
    region_page.check_corp_tarif_avaliable()


def test_hotel_in_cart(login_page, smartdesk_page, hotels_search_page, name_region_search, region_page, valid_user):
    """Проверка нахождения рейта в корзине после его добавления"""
    login_page.navigate_to_login_page()
    login_page.login(valid_user["username"], valid_user["password"])
    smartdesk_page.select_hotel_service()
    hotels_search_page.search_region_name(name_region_search)
    hotels_search_page.check_search_button_enabled()
    hotels_search_page.click_to_search_button()
    region_page.open_hotel_in_new_tab()
    region_page.wait_button_and_click()
    region_page.go_to_cart()

    cart_page = CartPage(region_page.page)
    cart_page.check_hotel_in_cart()
