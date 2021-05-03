from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_EMAIL = (By.NAME, "login-username")
    LOGIN_PASS = (By.NAME, "login-password")
    REG_EMAIL = (By.NAME, "registration-email")
    REG_PASS_1 = (By.NAME, "registration-password1")
    REG_PASS_2 = (By.NAME, "registration-password2")
