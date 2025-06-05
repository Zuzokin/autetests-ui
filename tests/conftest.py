import pytest
from playwright.sync_api import Playwright, Page
from typing import Generator


@pytest.fixture
def chromium_page(playwright: Playwright) -> Page: # type: ignore
    browser = playwright.chromium.launch(headless=False)
    yield browser.new_page()
    browser.close()


@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill('user.name@gmail.com')

    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill('username')

    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill('password')

    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    # Сохраняем состояние браузера (куки и localStorage) в файл для дальнейшего использования
    context.storage_state(path="browser-state.json")

    browser.close()


    # я бы добавил удаление файла browser-state.json после завершения тестовой сессии
    # но это не по ТЗ(тк нельзя использовать yield), 
    # поэтому я не стал его добавлять


@pytest.fixture()
def chromium_page_with_state(playwright: Playwright, initialize_browser_state: Page):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="browser-state.json")
    yield context.new_page()
    browser.close()

# есть еще одна идея решения этой задачи, но я не уверен что это хорошо так делать
# хоть я и уменьшаю дублирование кода
# но увеличивается сложность поддержки этого кода 
# тк использую самописную фукнцию вместо стадартного подхода
# поэтому оставляю первый вариант решения для


# import pytest
# from playwright.sync_api import Playwright, Page

# def launch_browser_and_context(playwright, storage_state=None):
#     browser = playwright.chromium.launch(headless=False)
#     if storage_state:
#         context = browser.new_context(storage_state=storage_state)
#     else:
#         context = browser.new_context()
#     return browser, context

# @pytest.fixture
# def chromium_page(playwright: Playwright) -> Page:
#     browser, context = launch_browser_and_context(playwright)
#     page = context.new_page()
#     yield page
#     browser.close()

# @pytest.fixture(scope="session")
# def initialize_browser_state(playwright: Playwright):
#     browser, context = launch_browser_and_context(playwright)
#     page = context.new_page()

#     page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

#     email_input = page.get_by_test_id('registration-form-email-input').locator('input')
#     email_input.fill('user.name@gmail.com')

#     username_input = page.get_by_test_id('registration-form-username-input').locator('input')
#     username_input.fill('username')

#     password_input = page.get_by_test_id('registration-form-password-input').locator('input')
#     password_input.fill('password')

#     registration_button = page.get_by_test_id('registration-page-registration-button')
#     registration_button.click()

#     # Сохраняем состояние браузера (куки и localStorage) в файл для дальнейшего использования
#     context.storage_state(path="browser-state.json")

#     browser.close()

# @pytest.fixture()
# def chromium_page_with_state(playwright: Playwright, initialize_browser_state):
#     browser, context = launch_browser_and_context(playwright, storage_state="browser-state.json")
#     yield context.new_page()
#     browser.close()