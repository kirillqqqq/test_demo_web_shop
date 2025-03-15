from selenium.webdriver.common.by import By


class LoginPageLocator:
    EMAIL = (By.XPATH, '//*[@id="Email"]')
    PASSWORD = (By.XPATH, '//*[@id="Password"]')
    LOGIN_BUTTON = (By.XPATH, '//*[@class="button-1 login-button"]')
    SUCCESS_LOGIN_STATUS = (By.XPATH, '//*[@class="header-links"]/descendant::a[1]')
    UN_SUCCESS_LOGIN_STATUS = (By.XPATH, '//*[@class="validation-summary-errors"]/descendant::li')

