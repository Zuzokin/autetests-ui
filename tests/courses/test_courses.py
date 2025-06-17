import allure
import pytest
from allure_commons.types import Severity

from pages.courses.courses_list_page import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage
from testdata.params.courses import CourseCardParams
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag


@pytest.mark.courses
@pytest.mark.regression
@allure.tag(AllureTag.REGRESSION, AllureTag.COURSES)
@allure.epic(AllureEpic.LMS) # Добавили epic
@allure.feature(AllureFeature.COURSES) # Добавили feature
@allure.story(AllureStory.COURSES) # Добавили story
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.COURSES)
class TestCourses:
    @allure.title("Check displaying of empty courses list")
    @allure.severity(Severity.NORMAL)
    def test_empty_courses_list(self, courses_list_page: CoursesListPage):
        courses_list_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        courses_list_page.sidebar.check_visible()
        courses_list_page.navbar.check_visible("username")

        courses_list_page.toolbar_view.check_visible()
        courses_list_page.check_visible_empty_view()

    @allure.title("Create course")
    @allure.severity(Severity.CRITICAL)
    def test_create_course(self, create_course_page: CreateCoursePage, courses_list_page: CoursesListPage):
        # 1. Открыть страницу создания курса
        create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")

        # 2-5. Проверка начального состояния страницы
        create_course_page.create_course_toolbar_view.check_visible(is_create_course_disabled=True)
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=False)

        # 6. Проверка формы создания курса

        create_course_page.create_course_form.check_visible(CourseCardParams(
            title="",
            max_score="0",
            min_score="0",
            estimated_time="",
            description=""
        ))

        # 7-9. Проверка раздела Exercises
        create_course_page.create_course_exercises_toolbar_view.check_visible()
        create_course_page.check_visible_exercises_empty_view()

        # 10-11. Загрузка изображения
        create_course_page.image_upload_widget.upload_preview_image('./testdata/files/image.png')
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)

        # 12. Заполнение формы курса
        create_course_page.create_course_form.fill(CourseCardParams(
            title="Playwright",
            max_score="100",
            min_score="10",
            estimated_time="2 weeks",
            description="Playwright"
        ))

        # 13. Создание курса
        create_course_page.create_course_toolbar_view.click_create_course_button()

        # 14-16. Проверки на странице списка курсов
        courses_list_page.toolbar_view.check_visible()

        # Проверка данных созданного курса
        courses_list_page.course_view.check_visible(CourseCardParams(
            index=0,
            title="Playwright",
            max_score="100",
            min_score="10",
            estimated_time="2 weeks",
            description="Playwright"
        ))

    @allure.severity(Severity.CRITICAL)
    @allure.title("Edit course")
    def test_edit_course(self, create_course_page: CreateCoursePage, courses_list_page: CoursesListPage):
        # 1. Открыть страницу создания курса
        create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")

        # 2. Загрузка изображения
        create_course_page.image_upload_widget.upload_preview_image('./testdata/files/image.png')
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)

        # 3. Заполнение формы курса
        initial_params = CourseCardParams(
            title="Playwright",
            max_score="100",
            min_score="10",
            estimated_time="2 weeks",
            description="Playwright"
        )
        create_course_page.create_course_form.fill(initial_params)

        # 4. Создание курса
        create_course_page.create_course_toolbar_view.click_create_course_button()

        # 5. Проверка, что курс появился на странице списка
        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.check_visible(initial_params)

        # 7. Открыть меню карточки и нажать Edit
        courses_list_page.course_view.menu.click_edit(0)

        # 8. Изменить все поля
        updated_params = CourseCardParams(
            title="Python",
            max_score="200",
            min_score="20",
            estimated_time="4 weeks",
            description="Python course updated"
        )
        create_course_page.create_course_form.fill(updated_params)

        # 9. Сохранить изменения (та же кнопка)
        create_course_page.create_course_toolbar_view.click_create_course_button()

        # 10. Проверить, что карточка обновилась
        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.check_visible(updated_params)


