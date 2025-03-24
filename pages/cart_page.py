import random

from locators.cart_page_locators import CartPageLocators as Locator
from locators.items_page_locators import ItemsPageLocators as Item_page_locator
from selenium.webdriver.support.ui import Select
import time


class CartPage:
    def __init__(self, browser):
        self.browser = browser
        self.url_books = 'https://demowebshop.tricentis.com/books'
        self.url_cart = 'https://demowebshop.tricentis.com/cart'

    def open_books(self):
        # Открытие браузера
        self.browser.get(self.url_books)

    def open_cart(self):
        # Открытие браузера
        self.browser.get(self.url_cart)

    def check_books_page(self):
        title = self.browser.find_element(*Item_page_locator.TITLE)
        assert 'Books' in title.text, f"Ожидаемый текст: Books, полученный текст: {title}"

    def add_to_cart(self):
        add_to_cart_buttons = self.browser.find_elements(*Item_page_locator.ADD_TO_CART)
        add_to_cart_button = add_to_cart_buttons[0]
        add_to_cart_button.click()
        time.sleep(1)
        add_to_cart_status = self.browser.find_element(*Item_page_locator.ADD_TO_CART_STATUS)
        assert 'The product has been added to your shopping cart' in add_to_cart_status.text, \
            f"Ожидаемое текст: The product has been added to your shopping cart, полученный текст: {add_to_cart_status.text}"

    def check_cart(self):
        cart_qty = self.browser.find_element(*Item_page_locator.CART_QTY)
        assert '1' in cart_qty.text, f"Ожидаемое количество: 1, полученное количество: {cart_qty.text}"

    def check_cart_page(self):
        title = self.browser.find_element(*Locator.TITLE)
        assert 'Shopping cart' in title.text, f"Ожидаемый текст: Books, полученный текст: {title}"

    def check_cart_on_cart_page(self):
        cart_qty = self.browser.find_elements(*Locator.CART_QTY)
        assert len(cart_qty) == 1, \
            f'Ожидаемое кол-во элементов 1, полученное кол-во элементов {len(cart_qty)}'
        cart_qty_value = int(cart_qty[0].get_attribute("value"))
        assert cart_qty_value == 1, \
            f'Ожидаемое кол-во элементов 1, полученное кол-во элементов {cart_qty_value}'

    def select_country(self):
        countries_list = self.browser.find_element(*Locator.COUNTRY_LIST)
        countries_list.click()
        countries = self.browser.find_elements(*Locator.COUNTRIES)
        filtered_countries = countries[1:]
        country = random.choice(filtered_countries)
        country.click()
        select = Select(countries_list)
        selected_country = select.first_selected_option.text
        assert country.text == selected_country, \
            f"Ожидаемый выбор {country.text} выбранный элемент {selected_country}"

    def checkout(self):
        term_of_service = self.browser.find_element(*Locator.TERMS_OF_SERVICE)
        term_of_service.click()
        checkout_button = self.browser.find_element(*Locator.CHECKOUT)
        checkout_button.click()
        time.sleep(1)
        title = self.browser.find_element(*Locator.TITLE)
        assert "Checkout" in title.text, \
            f"Ожидаемый текст: Checkout, полученный текст: {title}"

