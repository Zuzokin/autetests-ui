from playwright.sync_api import Page

from components.base_component import BaseComponent, expect
from testdata.params.courses import CourseCardParams


class CreateCourseFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.create_course_title_input = page.get_by_test_id('create-course-form-title-input').locator('input')
        self.create_course_estimated_time_input = (
            page.get_by_test_id('create-course-form-estimated-time-input').locator('input')
        )
        self.create_course_description_textarea = (
            page.get_by_test_id('create-course-form-description-input').locator('textarea').first
        )
        self.create_course_max_score_input = page.get_by_test_id('create-course-form-max-score-input').locator('input')
        self.create_course_min_score_input = page.get_by_test_id('create-course-form-min-score-input').locator('input')

    def check_visible(
            self,
            params: CourseCardParams
    ):
        expect(self.create_course_title_input).to_be_visible()
        expect(self.create_course_title_input).to_have_value(params.title)

        expect(self.create_course_estimated_time_input).to_be_visible()
        expect(self.create_course_estimated_time_input).to_have_value(params.estimated_time)

        expect(self.create_course_description_textarea).to_be_visible()
        expect(self.create_course_description_textarea).to_have_value(params.description)

        expect(self.create_course_max_score_input).to_be_visible()
        expect(self.create_course_max_score_input).to_have_value(params.max_score)

        expect(self.create_course_min_score_input).to_be_visible()
        expect(self.create_course_min_score_input).to_have_value(params.min_score)

    def fill(
            self,
            params: CourseCardParams
    ):
        self.create_course_title_input.fill(params.title)
        expect(self.create_course_title_input).to_have_value(params.title)

        self.create_course_estimated_time_input.fill(params.estimated_time)
        expect(self.create_course_estimated_time_input).to_have_value(params.estimated_time)

        self.create_course_description_textarea.fill(params.description)
        expect(self.create_course_description_textarea).to_have_value(params.description)

        self.create_course_max_score_input.fill(params.max_score)
        expect(self.create_course_max_score_input).to_have_value(params.max_score)

        self.create_course_min_score_input.fill(params.min_score)
        expect(self.create_course_min_score_input).to_have_value(params.min_score)
