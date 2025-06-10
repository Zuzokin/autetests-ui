from playwright.sync_api import Page, expect

from components.authentication.registration_form_component import RegistrationFormComponent
from pages.base_page import BasePage
from elements.input import Input
from elements.button import Button
from elements.link import Link


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.registration_form = RegistrationFormComponent(page)

        self.registration_button = Button(page, 'registration-page-registration-button', 'Registration Button')
        self.login_link = Link(page, 'registration-page-login-link', 'Login Link')

    def click_registration_button(self):
        self.registration_button.click()

    def click_login_link(self):
        self.login_link.click()
