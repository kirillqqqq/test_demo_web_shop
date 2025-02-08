import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture()
def browser():
    options = Options()
    options.add_argument('--headless')
    browser = webdriver.Chrome(options=options)
    browser.maximize_window()
    yield browser
    browser.quit()
