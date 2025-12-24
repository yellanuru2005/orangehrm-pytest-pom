from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):

    CHECKOUT_BTN = (By.ID, "checkout")
    CART_ITEM = (By.CLASS_NAME, "inventory_item_name")
    CART_TITLE = (By.CLASS_NAME, "title")  # <-- IMPORTANT

    def is_cart_page_loaded(self):
        return self.get_text(self.CART_TITLE) == "Your Cart"

    def is_item_present(self):
        return self.find(self.CART_ITEM).is_displayed()

    def click_checkout(self):
        self.click(self.CHECKOUT_BTN)
