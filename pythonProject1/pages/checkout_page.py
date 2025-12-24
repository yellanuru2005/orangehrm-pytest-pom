from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutPage(BasePage):

    # 🔹 PAGE IDENTIFIER
    PAGE_TITLE = (By.CLASS_NAME, "title")

    # 🔹 CHECKOUT INFORMATION PAGE
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")

    # 🔹 FINAL PAGE
    FINISH_BTN = (By.ID, "finish")
    SUCCESS_MSG = (By.CLASS_NAME, "complete-header")

    def wait_for_checkout_info_page(self):
        self.wait.until(
            lambda d: "Checkout" in self.get_text(self.PAGE_TITLE)
        )

    def enter_checkout_details(self, fname, lname, zip_code):
        self.wait_for_checkout_info_page()
        self.type(self.FIRST_NAME, fname)
        self.type(self.LAST_NAME, lname)
        self.type(self.POSTAL_CODE, zip_code)
        self.click(self.CONTINUE_BTN)

    def finish_checkout(self):
        self.click(self.FINISH_BTN)

    def get_success_message(self):
        return self.get_text(self.SUCCESS_MSG)
