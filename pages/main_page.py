


class MainPage:
    def __init__(self, browser):
        self.browser = browser
        self.url = "https://demowebshop.tricentis.com/"

    def open(self):
        self.browser.get(self.url)

    def get_title(self):
        return self.browser.title

    def check_title(self, expected_title):
        assert self.get_title() == expected_title, f"Expected '{expected_title}', but got '{self.get_title()}'"
