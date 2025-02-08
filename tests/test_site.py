from pages.main_page import MainPage
from selenium.webdriver.common.by import By



def test_open_site(browser):
    main_page = MainPage(browser)
    main_page.open()
    main_page.check_title('Demo Web Shop')



