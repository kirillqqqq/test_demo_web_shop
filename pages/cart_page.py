import random
import allure
from locators.cart_page_locators import CartPageLocators as Locator
from locators.items_page_locators import ItemsPageLocators as Item_page_locator
from pages.login_page import LoginPage
from selenium.webdriver.support.ui import Select
import time


class CartPage:
    def __init__(self, browser):
        self.browser = browser
        self.url_books = 'https://demowebshop.tricentis.com/books'
        self.url_cart = 'https://demowebshop.tricentis.com/cart'

    def open_books(self):
        # Открытие браузера
        with allure.step("Открываем страницу книги"):
            self.browser.get(self.url_books)

    def open_cart(self):
        # Открытие браузера
        with allure.step("Открываем страницу корзины"):
            self.browser.get(self.url_cart)

    def check_books_page(self):
        with allure.step("Проверяем заголовок страницы книги"):
            title = self.browser.find_element(*Item_page_locator.TITLE)
            assert 'Books' in title.text, f"Ожидаемый текст: Books, полученный текст: {title}"

    def add_to_cart(self):
        with allure.step("Добавляем элементы страницы клиги в корзину"):
            add_to_cart_buttons = self.browser.find_elements(*Item_page_locator.ADD_TO_CART)
            add_to_cart_button = add_to_cart_buttons[0]
            add_to_cart_button.click()
            time.sleep(1)
            add_to_cart_status = self.browser.find_element(*Item_page_locator.ADD_TO_CART_STATUS)
            assert 'The product has been added to your shopping cart' in add_to_cart_status.text, \
                f"Ожидаемое текст: The product has been added to your shopping cart, полученный текст: {add_to_cart_status.text}"

    def check_cart(self):
        with allure.step("Проверяем кол-во позиций в корзине"):
            cart_qty = self.browser.find_element(*Item_page_locator.CART_QTY)
            assert '1' in cart_qty.text, f"Ожидаемое количество: 1, полученное количество: {cart_qty.text}"

    def check_cart_page(self):
        with allure.step("Проверяем переход на страницу корзины"):
            title = self.browser.find_element(*Locator.TITLE)
            assert 'Shopping cart' in title.text, f"Ожидаемый текст: Books, полученный текст: {title}"

    def check_cart_on_cart_page(self):
        with allure.step("Проверяем кол-во добавленных товаров в корзине"):
            cart_qty = self.browser.find_elements(*Locator.CART_QTY)
            assert len(cart_qty) == 1, \
                f'Ожидаемое кол-во элементов 1, полученное кол-во элементов {len(cart_qty)}'
            cart_qty_value = int(cart_qty[0].get_attribute("value"))
            assert cart_qty_value == 1, \
                f'Ожидаемое кол-во элементов 1, полученное кол-во элементов {cart_qty_value}'

    """def select_country(self):
        with allure.step("Проверяем проверку выбора страны на странице корзины"):
            countries_list = self.browser.find_element(*Locator.COUNTRY_LIST)
            countries_list.click()
            countries = self.browser.find_elements(*Locator.COUNTRIES)
            filtered_countries = countries[1:]
            country = random.choice(filtered_countries)
            country.click()
            select = Select(countries_list)
            selected_country = select.first_selected_option.text
            assert country.text == selected_country, \
                f"Ожидаемый выбор {country.text} выбранный элемент {selected_country}"""

    def cart_to_checkout(self, email, password):
        with allure.step("Проверяем переход к chekout со страницы корзины"):
            term_of_service = self.browser.find_element(*Locator.TERMS_OF_SERVICE)
            term_of_service.click()
            checkout_button = self.browser.find_element(*Locator.CHECKOUT)
            checkout_button.click()
            time.sleep(1)
            title = self.browser.find_element(*Locator.TITLE)
            if "Welcome, Please Sign In!" in title.text:
                login_page = LoginPage(self.browser)
                login_page.login(email, password)
                term_of_service = self.browser.find_element(*Locator.TERMS_OF_SERVICE)
                term_of_service.click()
                checkout_button = self.browser.find_element(*Locator.CHECKOUT)
                checkout_button.click()
                time.sleep(1)
                title = self.browser.find_element(*Locator.TITLE)
            assert "Checkout" in title.text, \
                f"Ожидаемый текст: Checkout, полученный текст: {title.text}"

    def checkout_billing_address(self, city, address, postcode, phone):
        with allure.step("Оформляем заказ"):
            countries_list = self.browser.find_element(*Locator.NEW_COUNTRY_LIST)
            countries_list.click()
            countries = self.browser.find_elements(*Locator.NEW_COUNTRIES)
            filtered_countries = countries[1:]
            country = random.choice(filtered_countries)
            country.click()

            checkout_city = self.browser.find_element(*Locator.CITY)
            checkout_city.send_keys(f'{city}')

            checkout_address1 = self.browser.find_element(*Locator.ADDRESS1)
            checkout_address1.send_keys(f'{address}')

            checkout_postcode = self.browser.find_element(*Locator.POSTCODE)
            checkout_postcode.send_keys(f'{postcode}')

            checkout_phone = self.browser.find_element(*Locator.PHONE)
            checkout_phone.send_keys(f'{phone}')

            continue_button = self.browser.find_elements(*Locator.CONTINUE_BUTTON)
            continue_button = continue_button[0]
            continue_button.click()
            time.sleep(1)

            select_shipping_address = self.browser.find_element(*Locator.SELECT_SHIPPING_ADDRESS)
            assert select_shipping_address.is_displayed(), \
                "Выбранный адрес не отображается, не осуществлен переход к следующему шагу"

    def checkout_shipping_address(self):
        with allure.step("Адрес доставки"):
            continue_button = self.browser.find_elements(*Locator.CONTINUE_BUTTON)
            continue_button = continue_button[1]
            continue_button.click()
            time.sleep(1)
            shipping_method_list = self.browser.find_element(*Locator.SHIPPING_METHOD_LIST)
            assert shipping_method_list.is_displayed(), \
                "Способы доставки не отображаются, не осуществлен переход к следующему шагу"

    def checkout_shipping_method(self):
        with allure.step("Выбор способа доставки"):
            shipping_option = {
                "2nd day": Locator.SHIPPING_METHOD_SECOND_DAY,
                "Next day": Locator.SHIPPING_METHOD_NEXT_DAY,
                "Ground": Locator.SHIPPING_METHOD_GROUND
            }

            for order_by in ["2nd day",
                             "Next day",
                             "Ground"]:
                shipping_method_order_by = self.browser.find_element(*shipping_option[order_by])
                shipping_method_order_by.click()
                assert shipping_method_order_by.is_selected(), \
                        f"Способ оплаты {shipping_method_order_by.get_attribute('id')} не был выбран."

            continue_button = self.browser.find_elements(*Locator.CONTINUE_BUTTON)
            continue_button = continue_button[2]
            continue_button.click()
            time.sleep(1)
            payment_method_list = self.browser.find_element(*Locator.PAYMENT_METHOD_LIST)

            assert payment_method_list.is_displayed(), \
                "Способы оплаты не отображаются, не осуществлен переход к следующему шагу"

    def checkout_payment_method(self):
        with allure.step("Выбор способа оплаты"):
            payment_option = {
                "Check/ Money order": Locator.PAYMENT_METHOD_MONEY_ORDER,
                "Credit Card": Locator.PAYMENT_METHOD_CREDIT_CARD,
                "Purchase Order": Locator.PAYMENT_METHOD_PURCHASE_ORDER,
                "Cash On": Locator.PAYMENT_METHOD_CASH_ON
            }

            for order_by in ["Check/ Money order",
                             "Credit Card",
                             "Purchase Order",
                             "Cash On"]:
                payment_method_order_by = self.browser.find_element(*payment_option[order_by])
                payment_method_order_by.click()
                assert payment_method_order_by.is_selected(), \
                    f"Способ оплаты {payment_method_order_by.get_attribute('id')} не был выбран."

            continue_button = self.browser.find_elements(*Locator.CONTINUE_BUTTON)
            continue_button = continue_button[3]
            continue_button.click()
            time.sleep(1)
            payment_info = self.browser.find_element(*Locator.PAYMENT_INFO)

            assert payment_info.is_displayed(), \
                "Информация по оплате не отображается, не осуществлен переход к следующему шагу"

    def checkout_payment_info(self):
        with allure.step("Информация по оплате"):
            continue_button = self.browser.find_elements(*Locator.CONTINUE_BUTTON)
            continue_button = continue_button[4]
            continue_button.click()
            time.sleep(1)
            order_review = self.browser.find_element(*Locator.ORDER_REVIEW)

            assert order_review.is_displayed(), \
                "Информация по заказу не отображается, не осуществлен переход к следующему шагу"

    def checkout_confirm(self):
        with allure.step("Подтверждение заказа"):
            confirm_button = self.browser.find_element(*Locator.CONFIRM_BUTTON)
            confirm_button.click()
            time.sleep(1)
            order_status = self.browser.find_element(*Locator.ORDER_STATUS)

            assert "Your order has been successfully processed!" in order_status.text, \
                f"Ожидаемый статус: Your order has been successfully processed!, статус: {order_status.text}"

