def test_add_to_cart(login_page, inventory_page):
    login_page.login("standard_user", "secret_sauce")
    inventory_page.add_product_to_cart()
    assert inventory_page.get_cart_count() == 1
