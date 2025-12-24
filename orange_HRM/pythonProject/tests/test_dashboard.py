def test_logout(login_page, dashboard_page):
    login_page.login("Admin", "admin123")
    assert dashboard_page.is_dashboard_loaded()
    dashboard_page.logout()


def test_add(a, b):
    return a + b
print(test_add(10,20))
