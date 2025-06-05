from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

        self.PAGE_URL = "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login"

    def visit(self, url: str):
        self.page.goto(url, wait_until='networkidle')

    def reload(self): 
        self.page.reload(wait_until='domcontentloaded')

    def open(self):
        self.page.goto(self.PAGE_URL, wait_until='networkidle')