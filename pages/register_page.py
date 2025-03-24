from locators.register_page_locators import RegisterPageLocator as Loсator
from selenium import webdriver
browser = webdriver.Chrome()


class RegistrationPage:
    def __init__(self, browser):
        self.browser = browser
        self.url = 'https://demowebshop.tricentis.com/register'

    def open(self):
        #Открытие браузера
        self.browser.get(self.url)

    def registration(self, name, lastname, email, password):
        # ввод имени
        f_name = self.browser.find_element(*Loсator.FIRST_NAME)
        f_name.send_keys(f'{name}')
        # ввод фамилии
        l_name = self.browser.find_element(*Loсator.LAST_NAME)
        l_name.send_keys(f'{lastname}')
        # ввод почты
        mail = self.browser.find_element(*Loсator.EMAIL)
        mail.send_keys(f'{email}')
        # ввод пароля
        passw = self.browser.find_element(*Loсator.PASSWORD)
        passw.send_keys(f'{password}')
        # ввод подтверждения проля
        confirm_passw = self.browser.find_element(*Loсator.CONFIRM_PASSWORD)
        confirm_passw.send_keys(f'{password}')
        # клик на кнопку регистрации
        register_button = self.browser.find_element(*Loсator.REGISTER_BUTTON)
        register_button.click()

    def check_success_registration(self):
        # проверка успешной регистрации (после клика на кнопку ожидаем текст Your registration completed
        registration_status = self.browser.find_element(*Loсator.SUCCESS_REGISTRATION_STATUS)
        assert 'Your registration completed' in registration_status.text, f"Ожидаемый текст: Your registration completed, полученный текст: {registration_status}"


    def logout(self):
        logout = self.browser.find_element(*Loсator.LOGOUT_LOGIN)
        logout.click()
        login = self.browser.find_element(*Loсator.LOGOUT_LOGIN)
        assert "Log in" in login.text, \
            f"Ожидаемый текст: Log in, полученный текст: {login.text}"

