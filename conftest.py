import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from faker import Faker
import random
import string
import allure


@pytest.fixture(scope="session")
def browser():
    options = Options()
    # Добавляем опцию без заголовков
    options.add_argument('--headless')
    # Запускаем браузер без заголовков
    browser = webdriver.Chrome(options=options)
    # Устанавливаем неявное ожидание в 10 секунд
    browser.implicitly_wait(10)
    # Открываем браузер на полный экран
    browser.maximize_window()
    yield browser
    browser.quit()


@pytest.fixture(scope="session")
def random_user_data():
    fake = Faker("en_US")

    return {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.email(),
        "password": ''.join(random.choices(string.ascii_letters + string.digits, k=12)),
        "city": fake.city(),
        "address": fake.address(),
        "postcode": fake.postcode(),
        "phone": fake.phone_number(),
    }


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:  # Если тест упал
        driver = item.funcargs.get("browser")  # Получаем браузер из фикстуры
        if driver:
            allure.attach(driver.get_screenshot_as_png(),
                          name="Failure Screenshot",
                          attachment_type=allure.attachment_type.PNG)
