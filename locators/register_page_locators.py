from selenium.webdriver.common.by import By


class RegisterPageLocator:
    #Локаторы формы регистрации
    # имя
    FIRST_NAME = (By.XPATH, '//*[@id="FirstName"]')
    # фамилия
    LAST_NAME = (By.XPATH, '//*[@id="LastName"]')
    # почта
    EMAIL = (By.XPATH, '//*[@id="Email"]')
    # пароль
    PASSWORD = (By.XPATH, '//*[@id="Password"]')
    # подтверждение пароля
    CONFIRM_PASSWORD = (By.XPATH, '//*[@id="ConfirmPassword"]')
    # кнопка регистрации
    REGISTER_BUTTON = (By.XPATH, '//*[@id="register-button"]')
    # статус успешной регистрации
    SUCCESS_REGISTRATION_STATUS = (By.XPATH, '//*[@class = "result"]')
    # статус неуспешной регистрации
    UN_SUCCESS_REGISTRATION_STATUS = (By.XPATH, '//*[@class="validation-summary-errors"]/descendant::li')

    LOGOUT_LOGIN = (By.XPATH, '//*[@class="header-links"]/descendant::a[2]')
