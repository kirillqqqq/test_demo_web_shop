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

    def display_per_page(self):
        count_locator = {
            4: Locator.DISPLAY_PER_PAGE_4,
            8: Locator.DISPLAY_PER_PAGE_8,
            12: Locator.DISPLAY_PER_PAGE_12
        }
        for count in [4, 8, 12]:
            display_items = self.browser.find_element(*count_locator[count])
            display_items.click()
            displayed_items = self.browser.find_elements(*Locator.PRODUCT_ITEM)
            if len(displayed_items) < count:
                # Если отображаемых товаров меньше ожидаемого количества
                selected_display_per_page = self.browser.find_element(*Locator.SELECTED_DISPLAY_PER_PAGE)
                assert str(count) == selected_display_per_page.text, (
                f"Ожидаемое кол-во элементов: {count}, "
                f"полученное кол-во элементов: {len(displayed_items)}"
                )
            else:
                # Если отображаемых товаров столько же, сколько ожидается
                assert len(displayed_items) == count, (
                    f"Ожидаемое кол-во элементов: {count}, "
                    f"полученное кол-во элементов: {len(displayed_items)}"
                )

    def view_as(self):
        view_locator = {
            "List": Locator.VIEW_AS_LIST,
            "Grid": Locator.VIEW_AS_GRID
        }
        for view_option in ["List", "Grid"]:
            view_as = self.browser.find_element(*view_locator[view_option])
            view_as.click()
            selected_view_as = self.browser.find_element(*Locator.SELECTED_VIEW_AS)
            assert view_option in selected_view_as.text, \
                f"Ожидаемый текст: {view_option}, полученный текст: {selected_view_as}"


