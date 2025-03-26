from pages.apparel_shoes_page import ApparelShoesPage
import allure


@allure.feature("Display per apparel shoes page")
@allure.story("Проверка отображения кол-ва элементов на странице одежа и обувь")
@allure.title("Проверка отображения кол-ва элементов на странице одежа и обувь")
def test_display_per_apparel_shoes_page(browser):
    apparel_shoes_page = ApparelShoesPage(browser)
    apparel_shoes_page.open()
    apparel_shoes_page.check_apparel_shoes_page()
    apparel_shoes_page.display_per_page()


@allure.feature("View as apparel shoes page")
@allure.story("Проверка отображения элементов списком или сеткой")
@allure.title("Проверка отображения элементов списком или сеткой")
def test_view_as_apparel_shoes_page(browser):
    apparel_shoes_page = ApparelShoesPage(browser)
    apparel_shoes_page.open()
    apparel_shoes_page.check_apparel_shoes_page()
    apparel_shoes_page.view_as()
