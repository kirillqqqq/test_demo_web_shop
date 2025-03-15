from locators.login_page_locators import LoginPageLocator as Loсator


class LoginPage:
    def __init__(self, browser):
        self.browser = browser
        self.url = 'https://demowebshop.tricentis.com/login'

    def open(self):
        # Открытие браузера
        self.browser.get(self.url)

    def login(self, email, password):
        # ввод почты
        mail = self.browser.find_element(*Loсator.EMAIL)
        mail.send_keys(f'{email}')
        # ввод пароля
        passw = self.browser.find_element(*Loсator.PASSWORD)
        passw.send_keys(f'{password}')
        # клик на кнопку регистрации
        login_button = self.browser.find_element(*Loсator.LOGIN_BUTTON)
        login_button.click()

    def check_success_login(self, email):
        login_status = self.browser.find_element(*Loсator.SUCCESS_LOGIN_STATUS)
        assert f'{email}' in login_status.text, f"Ожидаемый текст: {email}, полученный текст: {login_status}"



