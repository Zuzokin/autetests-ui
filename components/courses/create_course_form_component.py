import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent, expect
from testdata.params.courses import CourseCardParams
from elements.input import Input
from elements.textarea import Textarea


class CreateCourseFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.create_course_title_input = Input(page, 'create-course-form-title-input', 'Title')
        self.create_course_estimated_time_input = Input(page, 'create-course-form-estimated-time-input', 'Estimated Time')
        self.create_course_description_textarea = Textarea(page, 'create-course-form-description-input', 'Description')
        self.create_course_max_score_input = Input(page, 'create-course-form-max-score-input', 'Max Score')
        self.create_course_min_score_input = Input(page, 'create-course-form-min-score-input', 'Min Score')

    def check_visible(
            self,
            params: CourseCardParams
    ):
        with allure.step(f'Check visible create course form with title "{params.title}"'):
            self.create_course_title_input.check_visible()
            self.create_course_title_input.check_have_value(params.title)

            self.create_course_estimated_time_input.check_visible()
            self.create_course_estimated_time_input.check_have_value(params.estimated_time)

            self.create_course_description_textarea.check_visible()
            self.create_course_description_textarea.check_have_value(params.description)

            self.create_course_max_score_input.check_visible()
            self.create_course_max_score_input.check_have_value(params.max_score)

            self.create_course_min_score_input.check_visible()
            self.create_course_min_score_input.check_have_value(params.min_score)

    def fill(
            self,
            params: CourseCardParams
    ):
        with allure.step(f'Fill create course form with title "{params.title}"'):
            self.create_course_title_input.fill(params.title)
            self.create_course_title_input.check_have_value(params.title)

            self.create_course_estimated_time_input.fill(params.estimated_time)
            self.create_course_estimated_time_input.check_have_value(params.estimated_time)

            self.create_course_description_textarea.fill(params.description)
            self.create_course_description_textarea.check_have_value(params.description)

            self.create_course_max_score_input.fill(params.max_score)
            self.create_course_max_score_input.check_have_value(params.max_score)

            self.create_course_min_score_input.fill(params.min_score)
            self.create_course_min_score_input.check_have_value(params.min_score)
