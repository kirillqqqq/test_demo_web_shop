from selenium.webdriver.common.by import By


class CartPageLocators:
    TITLE = (By.XPATH, '//h1')
    CART_QTY = (By.XPATH, '//*[@class="qty-input"]')
    COUNTRY_LIST = (By.XPATH, '//*[@id="CountryId"]')
    COUNTRIES = (By.XPATH, '//*[@id="CountryId"]/option')
    TERMS_OF_SERVICE = (By.XPATH, '//*[@id="termsofservice"]')
    CHECKOUT = (By.XPATH, '//*[@id="checkout"]')

