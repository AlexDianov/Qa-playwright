from pages.login_page import LoginPage
from pages.smartdesk_page import SmartdeskPage
from pages.hotels_search_page import SearchPage
from pages.region_page import RegionPage

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
    """Проверка отсутсвия на выдаче рейтов с бесплатной отменой"""
    login_page.navigate_to_login_page()
    login_page.login(valid_user["username"], valid_user["password"])
    smartdesk_page.select_hotel_service()
    hotels_search_page.search_region_name(name_region_search)
    hotels_search_page.check_search_button_enabled()
    hotels_search_page.click_to_search_button()
    region_page.check_corp_tarif_avaliable()

def test_add_hotel_in_cart(login_page, smartdesk_page, hotels_search_page, name_region_search, region_page, valid_user):
    """Проверка возможности положить рейт в корзину"""
    login_page.navigate_to_login_page()
    login_page.login(valid_user["username"], valid_user["password"])
    smartdesk_page.select_hotel_service()
    hotels_search_page.search_region_name(name_region_search)
    hotels_search_page.check_search_button_enabled()
    hotels_search_page.click_to_search_button()
    region_page.click_to_choose_room_button()
    region_page.wait_room_wrapper()
    region_page.wait_button()
    region_page.click_hotel_current_room_cart()
