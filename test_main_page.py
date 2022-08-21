from .pages.main_page import MainPage
from .pages.login_page import LoginPage

from selenium.webdriver.common.by import By
"""
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.should_be_login_link()          # выполняем метод страницы — проверяем есть ли ссылка на логин
    page.go_to_login_page
"""

def test_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.should_be_login_url()          # выполняем метод страницы — проверяем правильный ли адрес страницы
    page.should_be_login_form()          # выполняем метод страницы — проверяем наличие формы регисртрации
    page.should_be_register_form()          # выполняем метод страницы — проверяем наличие формы авторизации