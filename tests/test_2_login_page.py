from pages.login_page import LoginPage
import time
import allure


@allure.feature("Login")
@allure.story("Проверка успешной авторизации")
@allure.title("Проверка успешной авторизации")
def test_success_login(browser, random_user_data):
    email = random_user_data["email"]
    password = random_user_data["password"]
    login_page = LoginPage(browser)
    login_page.open()
    login_page.login(email, password)
    time.sleep(1)
    login_page.check_success_login(email)
