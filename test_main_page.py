import pytest

from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.locators import BasketPageLocators


@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/'
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, page.go_to_login_page())
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/'
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET)
    page.is_element_present(*BasketPageLocators.EMPTY_BASKET_MASSAGE)
