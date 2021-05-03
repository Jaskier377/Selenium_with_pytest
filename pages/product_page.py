import time
from .base_page import BasePage
from .locators import ProductPageLocator


class ProductPage(BasePage):
    def add_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocator.BASKET_BUTTON)
        basket_button.click()
        self.solve_quiz_and_get_code()

    def price_in_basket(self):
        price = self.browser.find_element(*ProductPageLocator.PRICE_IN_PRODUCT_PAGE).text
        print(price)
        price_in_basket = self.browser.find_element(*ProductPageLocator.PRICE_IN_BASKET).text
        print(price_in_basket)
        assert price == price_in_basket, "Wrong price"

    def name_of_product(self):
        product_name = self.browser.find_element(*ProductPageLocator.PRODUCT_NAME_ON_PAGE).text
        print(product_name)
        product_name_in_basket = self.browser.find_element(*ProductPageLocator.PRODUCT_NAME_IN_BASKET).text
        print(product_name_in_basket)
        assert product_name == product_name_in_basket, "Wrong product"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocator.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_dissapeared_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocator.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"






