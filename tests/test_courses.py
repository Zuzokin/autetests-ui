from playwright.sync_api import expect, Page
import pytest

#Открыть страницу https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration
#Заполнить форму регистрации и нажать на кнопку "Registration"
#Сохранить состояние браузера
#Создать новую сессию браузера. В контекст необходимо подставить сохраненное состояние
#Открыть страницу https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses. Страница "Courses" должна открыться без авторизации
#Проверить наличие и текст заголовка "Courses" 
#Проверить наличие и текст блока "There is no results"

@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):
    chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    # Проверяем наличие и текст заголовка "Courses"
    expect(chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')).to_have_text('Courses')

    # Проверяем наличие и текст блока "There is no results"
    expect(chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')).to_have_text('There is no results')