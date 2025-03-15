import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from faker import Faker
import random
import string


@pytest.fixture()
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
    # Создаем генератор случайных данных
    fake = Faker()
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.email()
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
    return first_name, last_name, email, password
