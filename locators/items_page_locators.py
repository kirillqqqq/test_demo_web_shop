from selenium.webdriver.common.by import By


class ItemsPageLocators:
    TITLE = (By.XPATH, '//h1')
    ADD_TO_CART = (By.XPATH, '//*[@value="Add to cart"]')
    CART_QTY = (By.XPATH, '//*[@class="cart-qty"]')
    ADD_TO_CART_STATUS = (By.XPATH, '//*[@class="content"]')
    PRODUCT_ORDER_BY = (By.XPATH, '//*[@id="products-orderby"]')
    SELECTED_ORDER_BY = (By.XPATH, '//*[@id="products-orderby"]/*[@selected="selected"]')
    SORT_BY_NAME_A_TO_Z = (By.XPATH, '//option[text()="Name: A to Z"]')
    SORT_BY_NAME_Z_TO_A = (By.XPATH, '//option[text()="Name: Z to A"]')
    SORT_BY_PRICE_LOW_TO_HIGH = (By.XPATH, '//option[text()="Price: Low to High"]')
    SORT_BY_PRICE_HIGH_TO_LOW = (By.XPATH, '//option[text()="Price: High to Low"]')
    SORT_BY_CREATED_ON = (By.XPATH, '//option[text()="Created on"]')
    SORT_BY_POSITION = (By.XPATH, '//option[text()="Position"]')
    DISPLAY_PER_PAGE_4 = (By.XPATH, '//option[text()="4"]')
    DISPLAY_PER_PAGE_8 = (By.XPATH, '//option[text()="8"]')
    DISPLAY_PER_PAGE_12 = (By.XPATH, '//option[text()="12"]')
    SELECTED_DISPLAY_PER_PAGE = (By.XPATH, '//option[text()="12"]')
    PRODUCT_ITEM = (By.XPATH, '//*[@class="product-item"]')
    VIEW_AS_GRID = (By.XPATH, '//option[text()="Grid"]')
    VIEW_AS_LIST = (By.XPATH, '//option[text()="List"]')
    SELECTED_VIEW_AS = (By.XPATH, '//*[@id="products-viewmode"]/*[@selected="selected"]')
