from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET), "Product in the basket, but should not"

    def should_be_empty_basket_massage(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MASSAGE), "There is no massage, but should"
