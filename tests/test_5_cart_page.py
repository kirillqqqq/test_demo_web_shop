from pages.cart_page import CartPage


def test_cart_qty(browser):
    cart_page = CartPage(browser)
    cart_page.open_books()
    cart_page.check_books_page()
    cart_page.add_to_cart()
    cart_page.check_cart()
    cart_page.open_cart()
    cart_page.check_cart_page()
    cart_page.check_cart_on_cart_page()


def test_country_select(browser):
    cart_page = CartPage(browser)
    cart_page.check_cart_page()
    cart_page.select_country()


def test_checkout(browser):
    cart_page = CartPage(browser)
    cart_page.check_cart_page()
    cart_page.checkout()
