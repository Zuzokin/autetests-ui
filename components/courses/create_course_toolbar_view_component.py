import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent, expect
from testdata.params.courses import CourseCardParams
from elements.text import Text
from elements.button import Button


class CreateCourseToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.create_course_title = Text(page, 'create-course-toolbar-title-text', 'Create Course')
        self.create_course_button = Button(page, 'create-course-toolbar-create-course-button', 'Create Course')

    def check_visible(self, is_create_course_disabled=True):
        with allure.step(f'Check visible create course toolbar with button {"disabled" if is_create_course_disabled else "enabled"}'):
            self.create_course_title.check_visible()
            self.create_course_title.check_have_text('Create course')

            self.create_course_button.check_visible()

            if is_create_course_disabled:
                self.create_course_button.check_disabled()
            else:
                self.create_course_button.check_enabled()

    def click_create_course_button(self):
        self.create_course_button.click()
