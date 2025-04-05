from selenium.webdriver.common.by import By


class CartPageLocators:
    TITLE = (By.XPATH, '//h1')
    CART_QTY = (By.XPATH, '//*[@class="qty-input"]')
    COUNTRY_LIST = (By.XPATH, '//*[@id="CountryId"]')
    COUNTRIES = (By.XPATH, '//*[@id="CountryId"]/option')
    TERMS_OF_SERVICE = (By.XPATH, '//*[@id="termsofservice"]')
    CHECKOUT = (By.XPATH, '//*[@id="checkout"]')
    CITY = (By.XPATH, '//*[@id="BillingNewAddress_City"]')
    ADDRESS1 = (By.XPATH, '//*[@id="BillingNewAddress_Address1"]')
    POSTCODE = (By.XPATH, '//*[@id="BillingNewAddress_ZipPostalCode"]')
    PHONE = (By.XPATH, '//*[@id="BillingNewAddress_PhoneNumber"]')
    CONTINUE_BUTTON = (By.XPATH, '//*[@value="Continue"]')
    SHIPPING_METHOD_LIST = (By.XPATH, '//*[@class="section shipping-method"]')
    SELECT_SHIPPING_ADDRESS = (By.XPATH, '//*[@id="checkout-step-shipping"]')
    SHIPPING_METHOD_GROUND = (By.XPATH, '//*[@id="shippingoption_0"]')
    SHIPPING_METHOD_NEXT_DAY = (By.XPATH, '//*[@id="shippingoption_1"]')
    SHIPPING_METHOD_SECOND_DAY = (By.XPATH, '//*[@id="shippingoption_2"]')
    PAYMENT_METHOD_LIST = (By.XPATH, '//*[@class="section payment-method"]')
    PAYMENT_INFO = (By.XPATH, '//*[@class="section payment-info"]')
    ORDER_REVIEW = (By.XPATH, '//*[@class="order-review-data"]')
    CONFIRM_BUTTON = (By.XPATH, '//*[@value="Confirm"]')
    ORDER_STATUS = (By.XPATH, '//*[@class="title"]')
    NEW_COUNTRY_LIST = (By.XPATH, '//*[@id="BillingNewAddress_CountryId"]')
    NEW_COUNTRIES = (By.XPATH, '//*[@id="BillingNewAddress_CountryId"]/option')
    PAYMENT_METHOD_CASH_ON = (By.XPATH, '//*[@id="paymentmethod_0"]')
    PAYMENT_METHOD_MONEY_ORDER = (By.XPATH, '//*[@id="paymentmethod_1"]')
    PAYMENT_METHOD_CREDIT_CARD = (By.XPATH, '//*[@id="paymentmethod_2"]')
    PAYMENT_METHOD_PURCHASE_ORDER = (By.XPATH, '//*[@id="paymentmethod_3"]')


