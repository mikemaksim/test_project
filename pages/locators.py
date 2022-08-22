from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    
# class MainPageLocators():
#    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    
class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BOOK_TITLE = (By.CSS_SELECTOR, ".product_main h1")
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main .price_color") 
    # ADD_TO_BASKET_BOOK_TITLE = (By.CSS_SELECTOR, ".btn-add-to-basket")
    IN_BASKET_BOOK_TITLE = (By.CSS_SELECTOR, ".alert:nth-child(1) strong")
    IN_BASKET_BOOK_PRICE = (By.CSS_SELECTOR, ".alert:nth-child(3) strong")
    
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")