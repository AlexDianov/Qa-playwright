import pytest
from pages.login_page import LoginPage
from pages.smartdesk_page import SmartdeskPage
from pages.hotels_search_page import SearchPage
from pages.region_page import RegionPage

@pytest.fixture
def valid_user():
    return {
        "username": "alex.dianov@smartway.today",
        "password": "Dialexpen92"
    }

@pytest.fixture
def invalid_user():
    return {
        "username": "alex.dianov@smartway.today",
        "password": "wrong_password"
    }


@pytest.fixture
def login_page(page):
    return LoginPage(page)

@pytest.fixture
def smartdesk_page(page):
    return SmartdeskPage(page)

@pytest.fixture
def hotels_search_page(page):
    return SearchPage(page)

@pytest.fixture
def region_page(page):
    return RegionPage(page)

@pytest.fixture
def name_region_search():
    return "Пенза"


