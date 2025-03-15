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
        add_to_cart_status = self.browser.find_element(*Locator.ADD_TO_CART_STATUS)
        assert 'The product has been added to your shopping cart' in add_to_cart_status.text, f"Ожидаемое текст: The product has been added to your shopping cart, полученный текст: {add_to_cart_status.text}"

    def check_cart(self):
        cart_qty = self.browser.find_element(*Locator.CART_QTY)
        assert '1' in cart_qty.text, f"Ожидаемое количество: 1, полученное количество: {cart_qty.text}"

    def sort_page_a_to_z(self):
        product_order_by = self.browser.find_element(*Locator.PRODUCT_ORDER_BY)
        product_order_by.click()
        product_order_by_option = self.browser.find_element(*Locator.SORT_BY_NAME_A_TO_Z)
        product_order_by_option.click()
        product_selected_order_by = self.browser.find_element(*Locator.SELECTED_ORDER_BY)
        assert 'Name: A to Z' in product_selected_order_by.text, f"Ожидаемое текст: Name: A to Z, полученный текст: {product_selected_order_by.text}"

    def sort_page_z_to_a(self):
        product_order_by = self.browser.find_element(*Locator.PRODUCT_ORDER_BY)
        product_order_by.click()
        product_order_by_option = self.browser.find_element(*Locator.SORT_BY_NAME_Z_TO_A)
        product_order_by_option.click()
        product_selected_order_by = self.browser.find_element(*Locator.SELECTED_ORDER_BY)
        assert 'Name: Z to A' in product_selected_order_by.text, f"Ожидаемое текст: Name: Z to A, полученный текст: {product_selected_order_by.text}"

    def sort_page_low_to_high(self):
        product_order_by = self.browser.find_element(*Locator.PRODUCT_ORDER_BY)
        product_order_by.click()
        product_order_by_option = self.browser.find_element(*Locator.SORT_BY_PRICE_LOW_TO_HIGH)
        product_order_by_option.click()
        product_selected_order_by = self.browser.find_element(*Locator.SELECTED_ORDER_BY)
        assert 'Price: Low to High' in product_selected_order_by.text, f"Ожидаемое текст: Price: Low to High, полученный текст: {product_selected_order_by.text}"

    def sort_page_high_to_low(self):
        product_order_by = self.browser.find_element(*Locator.PRODUCT_ORDER_BY)
        product_order_by.click()
        product_order_by_option = self.browser.find_element(*Locator.SORT_BY_PRICE_HIGH_TO_LOW)
        product_order_by_option.click()
        product_selected_order_by = self.browser.find_element(*Locator.SELECTED_ORDER_BY)
        assert 'Price: High to Low' in product_selected_order_by.text, f"Ожидаемое текст: Price: High to Low, полученный текст: {product_selected_order_by.text}"

    def sort_page_created_on(self):
        product_order_by = self.browser.find_element(*Locator.PRODUCT_ORDER_BY)
        product_order_by.click()
        product_order_by_option = self.browser.find_element(*Locator.SORT_BY_CREATED_ON)
        product_order_by_option.click()
        product_selected_order_by = self.browser.find_element(*Locator.SELECTED_ORDER_BY)
        assert 'Created on' in product_selected_order_by.text, f"Ожидаемое текст: Created on, полученный текст: {product_selected_order_by.text}"
