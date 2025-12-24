def test_leave_list_search_no_records(login_page, dashboard_page, leave_list_page):
    # Login
    login_page.login("Admin", "admin123")

    # Navigate to Leave List
    dashboard_page.navigate_to_leave_list()
    assert leave_list_page.is_leave_list_page_loaded()

    # Apply filters
    leave_list_page.set_from_date("2025-01-01")
    leave_list_page.set_to_date("2025-12-31")
    leave_list_page.select_pending_status()

    # Search
    leave_list_page.click_search()

    # Validation
    assert leave_list_page.is_no_records_displayed()
