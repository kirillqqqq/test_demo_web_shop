import time

from locators.items_page_locators import ItemsPageLocators as Locator


class BooksPage:
    def __init__(self, browser):
        self.browser = browser
        self.url = 'https://demowebshop.tricentis.com/books'

    def open(self):
        # Открытие браузера
        self.browser.get(self.url)

    def check_books_page(self):
        title = self.browser.find_element(*Locator.TITLE)
        assert 'Books' in title.text, f"Ожидаемый текст: Books, полученный текст: {title}"

    def add_to_cart(self):
        add_to_cart_buttons = self.browser.find_elements(*Locator.ADD_TO_CART)
        add_to_cart_button = add_to_cart_buttons[0]
        add_to_cart_button.click()
        time.sleep(1)
        add_to_cart_status = self.browser.find_element(*Locator.ADD_TO_CART_STATUS)
        assert 'The product has been added to your shopping cart' in add_to_cart_status.text, \
            f"Ожидаемое текст: The product has been added to your shopping cart, полученный текст: {add_to_cart_status.text}"

    def check_cart(self):
        cart_qty = self.browser.find_element(*Locator.CART_QTY)
        assert '1' in cart_qty.text, f"Ожидаемое количество: 1, полученное количество: {cart_qty.text}"

    def sort_page(self):
        order_option = {
            "Name: A to Z": Locator.SORT_BY_NAME_A_TO_Z,
            "Name: Z to A": Locator.SORT_BY_NAME_Z_TO_A,
            "Price: Low to High": Locator.SORT_BY_PRICE_LOW_TO_HIGH,
            "Price: High to Low": Locator.SORT_BY_PRICE_HIGH_TO_LOW,
            "Created on": Locator.SORT_BY_CREATED_ON,
            "Position": Locator.SORT_BY_POSITION
        }
        for order_by in ["Name: A to Z",
                         "Name: Z to A",
                         "Price: Low to High",
                         "Price: High to Low",
                         "Created on",
                         "Position"]:
            product_order_by = self.browser.find_element(*Locator.PRODUCT_ORDER_BY)
            product_order_by.click()
            product_order_by_option = self.browser.find_element(*order_option[order_by])
            product_order_by_option.click()
            product_selected_order_by = self.browser.find_element(*Locator.SELECTED_ORDER_BY).text
            assert product_selected_order_by == order_by, (
                f"Ожидаемое кол-во элементов: {order_by}, "
                f"полученное кол-во элементов: {product_selected_order_by}"
            )
