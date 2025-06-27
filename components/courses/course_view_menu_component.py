import allure
from playwright.sync_api import Page, expect

from components.base_component import BaseComponent


class CourseViewMenuItemComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.menu_button = page.get_by_test_id('course-view-menu-button')
        self.edit_menu_item = page.get_by_test_id('course-view-edit-menu-item')
        self.delete_menu_item = page.get_by_test_id('course-view-delete-menu-item')

    @allure.step('Open course menu at index "{index}" and click edit')
    def click_edit(self, index: int):
        self.menu_button.nth(index).click()

        expect(self.edit_menu_item.nth(index)).to_be_visible()
        self.edit_menu_item.nth(index).click()

    @allure.step('Open course menu at index "{index}" and click delete')
    def click_delete(self, index: int):
        self.menu_button.nth(index).click()

        expect(self.delete_menu_item.nth(index)).to_be_visible()
        self.delete_menu_item.nth(index).click()
