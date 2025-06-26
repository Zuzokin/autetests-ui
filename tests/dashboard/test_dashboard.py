import allure
import pytest
from allure_commons.types import Severity

from pages.dashboard.dashboard_page import DashboardPage
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag
from tools.routes import AppRoute
from config import settings


@pytest.mark.dashboard
@pytest.mark.regression
@allure.epic(AllureEpic.LMS)  # Добавили epic
@allure.feature(AllureFeature.DASHBOARD)  # Добавили feature
@allure.story(AllureStory.DASHBOARD)  # Добавили story
@allure.tag(AllureTag.REGRESSION, AllureTag.DASHBOARD)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.DASHBOARD)
class TestDashboard:
    @allure.severity(Severity.NORMAL)
    @allure.title("Check displaying of dashboard page")
    def test_dashboard_displaying(self, dashboard_page_with_state: DashboardPage):
        dashboard_page_with_state.visit(AppRoute.DASHBOARD)

        dashboard_page_with_state.sidebar.check_visible()
        dashboard_page_with_state.navbar.check_visible(settings.test_user.username)

        dashboard_page_with_state.dashboard_toolbar_view.check_visible()

        dashboard_page_with_state.courses_chart_view.check_visible("Courses")
        dashboard_page_with_state.students_chart_view.check_visible('Students')
        dashboard_page_with_state.scores_chart_view.check_visible("Scores")
        dashboard_page_with_state.activities_chart_view.check_visible("Activities")
