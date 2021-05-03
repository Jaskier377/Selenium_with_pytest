from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_EMAIL = (By.NAME, "login-username")
    LOGIN_PASS = (By.NAME, "login-password")
    REG_EMAIL = (By.NAME, "registration-email")
    REG_PASS_1 = (By.NAME, "registration-password1")
    REG_PASS_2 = (By.NAME, "registration-password2")


class ProductPageLocator():
    BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    PRICE_IN_PRODUCT_PAGE = (By.XPATH, '//div[@class="col-sm-6 product_main"]//p[@class="price_color"]')
    PRICE_IN_BASKET = (By.XPATH, '//*[@id="messages"]/div[3]/div/p[1]/strong')
    PRODUCT_NAME_ON_PAGE = (By.XPATH, "//h1")
    PRODUCT_NAME_IN_BASKET = (By.XPATH, "//*[@id='messages']/div[1]/div/strong")
