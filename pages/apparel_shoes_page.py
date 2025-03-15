from locators.items_page_locators import ItemsPageLocators as Locator


class ApparelShoesPage:
    def __init__(self, browser):
        self.browser = browser
        self.url = 'https://demowebshop.tricentis.com/apparel-shoes'

    def open(self):
        # Открытие браузера
        self.browser.get(self.url)

    def check_apparel_shoes_page(self):
        title = self.browser.find_element(*Locator.TITLE)
        assert 'Apparel & Shoes' in title.text, \
            f"Ожидаемый текст: Apparel & Shoes, полученный текст: {title}"

    def display_per_page_4(self):
        display_items = self.browser.find_element(*Locator.DISPLAY_PER_PAGE_4)
        display_items.click()
        displayed_items = self.browser.find_elements(*Locator.PRODUCT_ITEM)
        assert len(displayed_items) == 4, (
            f"Ожидаемое кол-во элементов: 4, "
            f"полученное кол-во элементов: {len(displayed_items)}"
        )

    def display_per_page_8(self):
        display_items = self.browser.find_element(*Locator.DISPLAY_PER_PAGE_8)
        display_items.click()
        displayed_items = self.browser.find_elements(*Locator.PRODUCT_ITEM)
        assert len(displayed_items) == 8, (
            f"Ожидаемое кол-во элементов: 8, "
            f"полученное кол-во элементов: {len(displayed_items)}"
        )

    def display_per_page_12(self):
        display_items = self.browser.find_element(*Locator.DISPLAY_PER_PAGE_12)
        display_items.click()
        displayed_items = self.browser.find_elements(*Locator.PRODUCT_ITEM)
        assert len(displayed_items) == 12, (
            f"Ожидаемое кол-во элементов: 12, "
            f"полученное кол-во элементов: {len(displayed_items)}"
        )

    def view_as_list(self):
        view_as = self.browser.find_element(*Locator.VIEW_AS_LIST)
        view_as.click()
        selected_view_as = self.browser.find_element(*Locator.SELECTED_VIEW_AS)
        assert 'List' in selected_view_as.text, \
            f"Ожидаемый текст: List, полученный текст: {selected_view_as}"

    def view_as_grid(self):
        view_as = self.browser.find_element(*Locator.VIEW_AS_GRID)
        view_as.click()
        selected_view_as = self.browser.find_element(*Locator.SELECTED_VIEW_AS)
        assert 'Grid' in selected_view_as.text, \
            f"Ожидаемый текст: Grid, полученный текст: {selected_view_as}"
