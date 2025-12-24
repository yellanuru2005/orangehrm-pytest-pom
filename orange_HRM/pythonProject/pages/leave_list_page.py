from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class LeaveListPage(BasePage):

    # 🔹 PAGE IDENTIFIERS (ROBUST)
    PAGE_HEADER = (By.XPATH, "//h6[contains(normalize-space(), 'Leave')]")
    SEARCH_BTN = (By.XPATH, "//button[@type='submit']")

    # 🔹 FILTER FIELDS
    FROM_DATE = (By.XPATH, "(//input[@placeholder='yyyy-mm-dd'])[1]")
    TO_DATE = (By.XPATH, "(//input[@placeholder='yyyy-mm-dd'])[2]")

    STATUS_DROPDOWN = (By.XPATH, "//label[text()='Show Leave with Status']/../following-sibling::div")
    STATUS_PENDING = (By.XPATH, "//span[text()='Pending Approval']")

    LEAVE_TYPE_DROPDOWN = (By.XPATH, "//label[text()='Leave Type']/../following-sibling::div")

    RESET_BTN = (By.XPATH, "//button[normalize-space()='Reset']")

    # 🔹 RESULTS
    NO_RECORDS = (By.XPATH, "//span[text()='No Records Found']")
    TABLE_ROWS = (By.XPATH, "//div[@class='oxd-table-body']/div")

    # 🔹 PAGE LOAD CHECK (IMPORTANT FIX)
    def is_leave_list_page_loaded(self):
        self.wait.until(EC.presence_of_element_located(self.PAGE_HEADER))
        self.wait.until(EC.element_to_be_clickable(self.SEARCH_BTN))
        return True

    # 🔹 ACTIONS
    def set_from_date(self, date):
        self.type(self.FROM_DATE, date)

    def set_to_date(self, date):
        self.type(self.TO_DATE, date)

    def select_pending_status(self):
        self.click(self.STATUS_DROPDOWN)
        self.click(self.STATUS_PENDING)

    def click_search(self):
        self.click(self.SEARCH_BTN)

    # 🔹 VALIDATIONS
    def is_no_records_displayed(self):
        return self.find(self.NO_RECORDS).is_displayed()

    def get_result_count(self):
        return len(self.driver.find_elements(*self.TABLE_ROWS))
