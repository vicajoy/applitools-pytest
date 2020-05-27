import pytest
from pages import LoginPage, HomePage


def test_login_form(browser):
    login_page = LoginPage(browser)
    assert login_page.page_title() == "Login Form"
    assert login_page.username_label() == "Username"
    assert login_page.is_username_icon_visible() is True
    assert login_page.password_label() == "Password"
    assert login_page.is_password_icon_visible() is True
    assert login_page.is_remember_me_visible() is True
    assert login_page.is_twitter_icon_visible() is True
    assert login_page.is_facebook_icon_visible() is True
    assert login_page.is_linkedin_icon_visible() is True


@pytest.mark.parametrize("username, password, expected_message",
                         [("", "", "Both Username and Password must be present"),
                          ("user", "", "Password must be present"), ("", "pass", "Username must be present")])
def test_data_driven(browser, username, password, expected_message):
    login_page = LoginPage(browser)
    login_page.login_user(username, password)
    assert login_page.login_error_message() == expected_message
    login_page.login_user("user", "pass")
    assert HomePage(browser).is_logo_visible() is True


def test_table_sort(browser):
    login_page = LoginPage(browser)
    home_page = HomePage(browser)
    login_page.login_user("aaa", "aaa")
    assert home_page.are_amounts_equal() is True
