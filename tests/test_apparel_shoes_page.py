from pages.apparel_shoes_page import ApparelShoesPage


def test_display_per_apparel_shoes_page(browser):
    apparel_shoes_page = ApparelShoesPage(browser)
    apparel_shoes_page.open()
    apparel_shoes_page.check_apparel_shoes_page()
    apparel_shoes_page.display_per_page()


def test_view_as_apparel_shoes_page(browser):
    apparel_shoes_page = ApparelShoesPage(browser)
    apparel_shoes_page.open()
    apparel_shoes_page.check_apparel_shoes_page()
    apparel_shoes_page.view_as()
