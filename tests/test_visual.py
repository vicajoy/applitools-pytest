import pytest
from pages import LoginPage, HomePage, ExpensesPage


def test_login_form(browser, eyes):
    eyes.open(browser, "Applitools Demo", "Login Form Test")
    eyes.check_window("Login Form Page")
    eyes.close()


@pytest.mark.parametrize("username, password, screenshot_title",
                         [("", "", "Username and password are not entered"),
                          ("user", "", "Password is not entered"), ("", "pass", "Username is not entered"),
                          ("", "pass", "Login successfully")])
def test_data_driven(browser, eyes, username, password, screenshot_title):
    eyes.open(browser, "Applitools Demo", "Data Driven Test")
    login_page = LoginPage(browser)
    login_page.login_user(username, password)
    eyes.check_window(screenshot_title)
    eyes.close()


def test_data_driven(browser, username, password, expected_message):
    login_page = LoginPage(browser)
    login_page.login_user(username, password)
    assert login_page.login_error_message() == expected_message


def test_table_sort(browser, eyes):
    eyes.open(browser, "Applitools Demo", "Table Sort Test")
    home_page = HomePage(browser)
    LoginPage(browser).login_user("aaa", "aaa")
    eyes.check_window("Before sorting")
    home_page.sort_table_items()
    eyes.check_window("After sorting")
    eyes.close()


def test_canvas_chart(browser, eyes):
    eyes.open(browser, "Applitools Demo", "Canvas Chart Test")
    home_page = HomePage(browser)
    expenses_page = ExpensesPage(browser)
    LoginPage(browser).login_user("aaa", "aaa")
    home_page.compare_expenses()
    eyes.check_window("Data for one year")
    expenses_page.show_data_for_next_year()
    eyes.check_window("Data for two years")
    eyes.close()


def test_dynamic_content(browser, url, eyes):
    eyes.open(browser, "Applitools Demo", "Dynamic Content Test")
    new_url = url + "?showAd=true"
    HomePage(browser).go_to_page(new_url)
    LoginPage(browser).login_user("aaa", "aaa")
    eyes.check_window("Two gifs")
    eyes.close()
