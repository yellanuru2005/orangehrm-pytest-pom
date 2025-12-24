import pytest
from utils.driver_factory import get_driver
from config.config import BASE_URL
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@pytest.fixture(scope="function")
def setup():
    driver = get_driver()
    driver.get(BASE_URL)
    yield driver
    driver.quit()

@pytest.fixture
def login_page(setup):
    return LoginPage(setup)

@pytest.fixture
def inventory_page(setup):
    return InventoryPage(setup)

@pytest.fixture
def cart_page(setup):
    return CartPage(setup)

@pytest.fixture
def checkout_page(setup):
    return CheckoutPage(setup)
