import pytest
from pages.login_page import LoginPage
from pages.smartdesk_page import SmartdeskPage
from pages.hotels_search_page import SearchPage
from pages.region_page import RegionPage
from playwright.sync_api import expect
from dataclasses import dataclass

@dataclass
class User:
    login: str
    password: str

@pytest.fixture(autouse=True)
def set_default_timeout(page):
    page.set_default_timeout(10000)
    expect.set_options(timeout=10000)

@pytest.fixture
def valid_user():
    return User(
        login = "alex.dianov@smartway.today",
        password = "Dialexpen92"
    )


@pytest.fixture
def invalid_user():
    return User (
        login = "alex.dianov@smartway.today",
        password = "wrong_password"
    )


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
