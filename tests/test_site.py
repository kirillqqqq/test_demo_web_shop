import time

from pages.register_page import RegistrationPage
from pages.login_page import LoginPage
from pages.books_page import BooksPage
from pages.apparel_shoes_page import ApparelShoesPage


def test_success_registration(browser, random_user_data):
    first_name, last_name, email, password = random_user_data
    registration_page = RegistrationPage(browser)
    registration_page.open()
    registration_page.registration(first_name, last_name, email, password)
    registration_page.check_success_registration()


def test_success_login(browser, random_user_data):
    first_name, last_name, email, password = random_user_data
    login_page = LoginPage(browser)
    login_page.open()
    login_page.login(email, password)
    time.sleep(3)
    login_page.check_success_login(email)


def test_add_to_cart_books(browser):
    books_page = BooksPage(browser)
    books_page.open()
    books_page.check_books_page()
    books_page.add_to_cart()
    time.sleep(3)
    books_page.check_cart()


def test_sort_books_page(browser):
    books_page = BooksPage(browser)
    books_page.open()
    books_page.check_books_page()
    books_page.sort_page_a_to_z()
    books_page.sort_page_z_to_a()
    books_page.sort_page_low_to_high()
    books_page.sort_page_high_to_low()
    books_page.sort_page_created_on()


def test_display_per_apparel_shoes_page(browser):
    apparel_shoes_page = ApparelShoesPage(browser)
    apparel_shoes_page.open()
    apparel_shoes_page.check_apparel_shoes_page()
    apparel_shoes_page.display_per_page_4()
    apparel_shoes_page.display_per_page_8()
    apparel_shoes_page.display_per_page_12()


def test_view_as_apparel_shoes_page(browser):
    apparel_shoes_page = ApparelShoesPage(browser)
    apparel_shoes_page.open()
    apparel_shoes_page.check_apparel_shoes_page()
    apparel_shoes_page.view_as_list()
    apparel_shoes_page.view_as_grid()
