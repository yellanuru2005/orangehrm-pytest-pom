def test_valid_login(login_page, dashboard_page):
    login_page.login("Admin", "admin123")
    assert dashboard_page.is_dashboard_loaded()


def test_invalid_login(login_page):
    login_page.login("Admin", "wrongpass")
    assert "Invalid credentials" in login_page.get_error_message()
