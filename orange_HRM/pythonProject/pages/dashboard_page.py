from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DashboardPage(BasePage):

    HEADER = (By.XPATH, "//h6[text()='Dashboard']")
    USER_DROPDOWN = (By.CLASS_NAME, "oxd-userdropdown-name")
    LOGOUT = (By.XPATH, "//a[text()='Logout']")
    LEAVE_MENU = (By.XPATH, "//span[text()='Leave']")
    LEAVE_LIST = (By.XPATH, "//a[text()='Leave List']")

    def is_dashboard_loaded(self):
        return self.find(self.HEADER).is_displayed()

    def logout(self):
        self.click(self.USER_DROPDOWN)
        self.click(self.LOGOUT)

    def navigate_to_leave_list(self):
        self.click(self.LEAVE_MENU)
        self.click(self.LEAVE_LIST)

