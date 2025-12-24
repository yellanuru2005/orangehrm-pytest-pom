def test_valid_login(login_page):
    login_page.login("standard_user", "secret_sauce")
