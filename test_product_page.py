import random
from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
import pytest
from selenium import webdriver
import time


@pytest.mark.need_review
@pytest.mark.parametrize('links', ['0', '1', '2', '3', '4', '5', '6', pytest.param("7", marks=pytest.mark.xfail), '8', '9'])
def test_guest_can_add_product_to_basket(browser, links):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{links}'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.price_in_basket()
    page.name_of_product()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_dissapeared_of_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, page.go_to_login_page())
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.should_not_be_product_in_basket()
    page.should_be_empty_basket_massage()


@pytest.mark.need_review
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        email = str(time.time()) + "@fakemail.org"
        password = random.randint(100000000, 999999999)
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        self.browser = webdriver.Chrome()
        page = LoginPage(self.browser, link)
        page.open()
        page.register_new_user(email, password)
        page.should_be_authorized_user()
        yield
        self.browser.quit()

    def test_user_cant_see_success_message(self):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'
        page = ProductPage(self.browser, link)
        page.open()
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'
        page = ProductPage(self.browser, link)
        page.open()
        page.add_to_basket()
        page.price_in_basket()
        page.name_of_product()
