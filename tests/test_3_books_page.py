from pages.books_page import BooksPage
import time


def test_add_to_cart_books(browser):
    books_page = BooksPage(browser)
    books_page.open()
    books_page.check_books_page()



def test_sort_books_page(browser):
    books_page = BooksPage(browser)
    books_page.open()
    books_page.check_books_page()
    books_page.sort_page()


def test_display_per_books_page(browser):
    books_page = BooksPage(browser)
    books_page.open()
    books_page.check_books_page()
    books_page.display_per_page()
