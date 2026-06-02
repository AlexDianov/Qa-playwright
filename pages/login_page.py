from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator('[data-qa="sign-in-email-input"]')
        self.password_input = page.locator('[data-qa="sign-in-password-input"]')
        self.login_button = page.locator('[data-qa="sign-in-form-button"]')
        self.login_error = page.get_by_text("Неверно введены данные для входа")

    def navigate_to_login_page(self):
        """Открывает страницу логина."""
        self.page.goto('https://rc.gospodaprogrammisty.ru/')

    def login(self, username, password):
        """Выполняет вход с заданными учетными данными."""
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def check_login_failed(self):
        expect(
            self.login_error,
            "Неверно введены данные для входа"
        ).to_be_visible(timeout=10000)
        expect(
            self.login_error
        ).to_have_text("Неверно введены данные для входа")