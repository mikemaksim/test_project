from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def no_goods_are_in_basket(self):
        # Проверяет, что в корзине ничего нет
        assert self.is_not_element_present(*BasketPageLocators.BASKET_GOODS), "There are goods in basket"
    def message_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY_TEXT), "No message that basket is empty"