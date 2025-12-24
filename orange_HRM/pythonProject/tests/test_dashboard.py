def test_logout(login_page, dashboard_page):
    login_page.login("Admin", "admin123")
    assert dashboard_page.is_dashboard_loaded()
    dashboard_page.logout()
