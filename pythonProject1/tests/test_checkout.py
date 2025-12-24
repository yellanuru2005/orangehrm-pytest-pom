def test_complete_checkout(login_page, inventory_page, cart_page, checkout_page):
    login_page.login("standard_user", "secret_sauce")

    inventory_page.add_product_to_cart()
    inventory_page.go_to_cart()

    assert cart_page.is_cart_page_loaded()
    assert cart_page.is_item_present()

    cart_page.click_checkout()

    checkout_page.enter_checkout_details("Yashoda", "K", "500001")
    checkout_page.finish_checkout()

    assert checkout_page.get_success_message() == "Thank you for your order!"
