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


@allure.feature("Checkout")
@allure.story("Оформление заказа")
@allure.title("Оформление заказа")
def test_checkout(browser, random_user_data):
    email = random_user_data["email"]
    password = random_user_data["password"]
    city = random_user_data["city"]
    address = random_user_data["address"]
    postcode = random_user_data["postcode"]
    phone = random_user_data["phone"]

    cart_page = CartPage(browser)
    cart_page.check_cart_page()
    cart_page.cart_to_checkout(email, password)
    cart_page.checkout_billing_address(city, address, postcode, phone)
    cart_page.checkout_shipping_address()
    cart_page.checkout_shipping_method()
    cart_page.checkout_payment_method()
    cart_page.checkout_payment_info()
    cart_page.checkout_confirm()
