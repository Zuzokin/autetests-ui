from playwright.sync_api import expect, Page
import pytest

from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage
from testdata.params.courses import CourseCardParams


# Открыть страницу https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration
# Заполнить форму регистрации и нажать на кнопку "Registration"
# Сохранить состояние браузера
# Создать новую сессию браузера. В контекст необходимо подставить сохраненное состояние
# Открыть страницу https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses. Страница "Courses" должна открыться без авторизации
# Проверить наличие и текст заголовка "Courses"
# Проверить наличие и текст блока "There is no results"

@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):
    chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    # Проверяем наличие и текст заголовка "Courses"
    expect(chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')).to_have_text('Courses')

    # Проверяем наличие и текст блока "There is no results"
    expect(chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')).to_have_text(
        'There is no results')


@pytest.mark.courses
@pytest.mark.regression
def test_create_course(create_course_page: CreateCoursePage, courses_list_page: CoursesListPage):
    # 1. Открыть страницу создания курса
    create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")

    # 2-5. Проверка начального состояния страницы
    create_course_page.check_visible_create_course_title()
    create_course_page.check_disabled_create_course_button()
    create_course_page.check_visible_image_preview_empty_view()
    create_course_page.check_visible_image_upload_view()

    # 6. Проверка формы создания курса

    create_course_page.check_visible_create_course_form(CourseCardParams(
        title="",
        max_score="0",
        min_score="0",
        estimated_time="",
        description=""
    ))

    # 7-9. Проверка раздела Exercises
    create_course_page.check_visible_exercises_title()
    create_course_page.check_visible_create_exercise_button()
    create_course_page.check_visible_exercises_empty_view()

    # 10-11. Загрузка изображения
    create_course_page.upload_preview_image("./testdata/files/image.png")
    create_course_page.check_visible_image_upload_view(is_image_uploaded=True)

    # 12. Заполнение формы курса
    create_course_page.fill_create_course_form(CourseCardParams(
        title="Playwright",
        max_score="100",
        min_score="10",
        estimated_time="2 weeks",
        description="Playwright"
    ))

    # 13. Создание курса
    create_course_page.click_create_course_button()

    # 14-16. Проверки на странице списка курсов
    courses_list_page.check_visible_courses_title()
    courses_list_page.check_visible_create_course_button()

    # Проверка данных созданного курса
    courses_list_page.check_visible_course_card(CourseCardParams(
        index=0,
        title="Playwright",
        max_score="100",
        min_score="10",
        estimated_time="2 weeks",
        description="Playwright"
    ))
