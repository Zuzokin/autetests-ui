from playwright.sync_api import sync_playwright, expect, Page
import pytest

from pages.login_page import LoginPage

TEST_DATA = {
    "invalid_email_and_password": ("user.name@gmail.com", "password"),
    "invalid_email_and_empty_password": ("user.name@gmail.com", "  "),
    "empty_email_and_invalid_password": ("  ", "password"),
}


@pytest.mark.parametrize(
    "email,password",
    TEST_DATA.values(),
    ids=TEST_DATA.keys()
)
@pytest.mark.regression
@pytest.mark.authorization
def test_wrong_email_or_password_authorization(login_page: LoginPage, email: str, password: str):
    login_page.open()
    login_page.check_visible_login_title()
    login_page.fill_login_form(email=email, password=password)
    login_page.click_login_button()
    login_page.check_visible_wrong_email_or_password_alert()
