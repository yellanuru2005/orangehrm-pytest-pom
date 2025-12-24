from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):

    ADD_TO_CART_BTN = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    CART_TITLE = (By.CLASS_NAME, "title")

    # def add_product_to_cart(self):
    #     self.click(self.ADD_TO_CART_BTN)
    def add_product_to_cart(self):
        self.click(self.ADD_TO_CART_BTN)

    def get_cart_count(self):
        return int(self.get_text(self.CART_BADGE))

    def go_to_cart(self):
        self.click(self.CART_ICON)
        self.wait.until(lambda d: self.get_text(self.CART_TITLE) == "Your Cart")
