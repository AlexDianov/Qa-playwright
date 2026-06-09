from playwright.sync_api import Page


class start_page:
    def __init__(self, page: Page):
        self.page = page
        self.start_url = "https://rc.gospodaprogrammisty.ru/"

    def go_to_site(self):
        """Переход на сайт"""
        self.page.goto(self.start_url, wait_until="networkidle")
