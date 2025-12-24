import pytest
from utils.driver_factory import get_driver
from config.config import BASE_URL
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

@pytest.fixture
def setup():
    driver = get_driver()
    driver.get(BASE_URL)
    yield driver
    driver.quit()

@pytest.fixture
def login_page(setup):
    return LoginPage(setup)

@pytest.fixture
def dashboard_page(setup):
    return DashboardPage(setup)


from pages.leave_list_page import LeaveListPage

@pytest.fixture
def leave_list_page(setup):
    return LeaveListPage(setup)
