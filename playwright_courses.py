from playwright.sync_api import sync_playwright, expect

#Открыть страницу https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration
#Заполнить форму регистрации и нажать на кнопку "Registration"
#Сохранить состояние браузера
#Создать новую сессию браузера. В контекст необходимо подставить сохраненное состояние
#Открыть страницу https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses. Страница "Courses" должна открыться без авторизации
#Проверить наличие и текст заголовка "Courses" 
#Проверить наличие и текст блока "There is no results"

with sync_playwright() as playwright:
    # Запускаем Chromium браузер в обычном режиме (не headless)
    browser = playwright.chromium.launch(headless=False)
    # Создаем новый контекст браузера (новая сессия, которая изолирована от других)
    context = browser.new_context()
    # Открываем новую страницу в рамках контекста
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

    # Закрываем текущую страницу
    page.close()

    # Создаем новую сессию браузера с сохраненным состоянием
    context = browser.new_context(storage_state="browser-state.json")
    page = context.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    # Проверяем наличие и текст заголовка "Courses"
    expect(page.get_by_test_id('courses-list-toolbar-title-text')).to_have_text('Courses')

    # Проверяем наличие и текст блока "There is no results"
    expect(page.get_by_test_id('courses-list-empty-view-title-text')).to_have_text('There is no results')

    # Задержка для наглядности выполнения теста 
    page.wait_for_timeout(5000)

