from pages.login_page import LoginPage
import time


def test_success_login(browser, random_user_data):
    first_name, last_name, email, password = random_user_data
    login_page = LoginPage(browser)
    login_page.open()
    login_page.login(email, password)
    time.sleep(3)
    login_page.check_success_login(email)
