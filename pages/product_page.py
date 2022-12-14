from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException # в начале файла
import math

        
class ProductPage(BasePage):
    def add_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_button.click()
    
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
            
    def check_alert(self):
        self.book_title_coincide()
        self.book_price_coincide()
    
    def book_title_coincide(self):
        assert self.get_book_title() == self.get_in_basket_book_title(), f'Book titles differ'
        
    def book_price_coincide(self):
        assert self.get_book_price() == self.get_in_basket_book_price(), f'Book prices differ'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"
        
    def success_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message did not disappear"
       
    def get_book_title(self):
        book_title = self.browser.find_element(*ProductPageLocators.BOOK_TITLE).text
        return book_title
    
    def get_book_price(self):
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        return book_price    
        
    def get_in_basket_book_title(self):
        in_basket_book_title = self.browser.find_element(*ProductPageLocators.IN_BASKET_BOOK_TITLE).text
        return in_basket_book_title    
    
    def get_in_basket_book_price(self):
        in_basket_book_price = self.browser.find_element(*ProductPageLocators.IN_BASKET_BOOK_PRICE).text
        return in_basket_book_price    
   