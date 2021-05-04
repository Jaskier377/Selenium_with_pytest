from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "This is not LOGIN page"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL), "Login email is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASS), "Login password is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_EMAIL), "Registration email is not presented"
        assert self.is_element_present(*LoginPageLocators.REG_PASS_1), "Registration password is not presented"
        assert self.is_element_present(*LoginPageLocators.REG_PASS_2), "Registration confirmation password not " \
                                                                       "presented "

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REG_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REG_PASS_1).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_PASS_2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_BUTTON).click()
