from pages.cart_page import CartPage
import allure


@allure.feature("Cart qty")
@allure.story("Проверка ко-ва элементов в корзине")
@allure.title("Проверка ко-ва элементов в корзине")
def test_cart_qty(browser):
    cart_page = CartPage(browser)
    cart_page.open_books()
    cart_page.check_books_page()
    cart_page.add_to_cart()
    cart_page.check_cart()
    cart_page.open_cart()
    cart_page.check_cart_page()
    cart_page.check_cart_on_cart_page()


@allure.feature("Country select")
@allure.story("Проверка выбора страны в корзине")
@allure.title("Проверка выбора страны в корзине")
def test_country_select(browser):
    cart_page = CartPage(browser)
    cart_page.check_cart_page()
    cart_page.select_country()


@allure.feature("Checkout")
@allure.story("Проверка перехода на страницу оплаты из козины")
@allure.title("Проверка перехода на страницу оплаты из козины")
def test_checkout(browser):
    cart_page = CartPage(browser)
    cart_page.check_cart_page()
    cart_page.checkout()
