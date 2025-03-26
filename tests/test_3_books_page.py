from pages.books_page import BooksPage
import allure


@allure.feature("Add to cart books")
@allure.story("Проверка добавления элемента в корзину на странице книги")
@allure.title("Проверка добавления элемента в корзину на странице книги")
def test_add_to_cart_books(browser):
    books_page = BooksPage(browser)
    books_page.open()
    books_page.check_books_page()


@allure.feature("Sort books page")
@allure.story("Сортировки элементов на странице книги")
@allure.title("Сортировки элементов на странице книги")
def test_sort_books_page(browser):
    books_page = BooksPage(browser)
    books_page.open()
    books_page.check_books_page()
    books_page.sort_page()


@allure.feature("Display per books page")
@allure.story("Проверка отображения кол-ва элементов на странице книги")
@allure.title("Проверка отображения кол-ва элементов на странице книги")
def test_display_per_books_page(browser):
    books_page = BooksPage(browser)
    books_page.open()
    books_page.check_books_page()
    books_page.display_per_page()
