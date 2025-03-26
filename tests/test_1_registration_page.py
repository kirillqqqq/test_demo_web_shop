import allure
from pages.register_page import RegistrationPage


@allure.feature("Registration")
@allure.story("Успешная регистрация нового пользователя")
@allure.title("Регистрация")
def test_success_registration(browser, random_user_data):
    first_name, last_name, email, password = random_user_data
    registration_page = RegistrationPage(browser)
    registration_page.open()
    registration_page.registration(first_name, last_name, email, password)
    registration_page.check_success_registration()


@allure.feature("Registration")
@allure.story("Выход из системы")
@allure.title("Выход после регистрации")
def test_logout(browser):
    registration_page = RegistrationPage(browser)
    registration_page.logout()
