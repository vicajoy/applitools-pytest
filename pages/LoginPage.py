from selenium.common.exceptions import NoSuchElementException


class LoginPage:

    __page_title = ".auth-header"
    __username_icon = ".os-icon-user-male-circle"
    __password_icon = ".os-icon-fingerprint"
    __twitter_icon = "img[src='img/social-icons/twitter.png']"
    __facebook_icon = "img[src='img/social-icons/facebook.png']"
    __linkedin_icon = "img[src='img/social-icons/linkedin.png']"
    __remember_me = ".form-check-label"
    __username_label = "//input[@id='username']/../label"
    __password_label = "//input[@id='password']/../label"
    __login_btn = "#log-in"
    __login_error = ".alert-warning"
    __username = "#username"
    __password = "#password"

    def __init__(self, driver):
        self.driver = driver

    def page_title(self):
        return self.driver.find_element_by_css_selector(LoginPage.__page_title).text

    def username_label(self):
        return self.driver.find_element_by_xpath(LoginPage.__username_label).text

    def is_username_icon_visible(self):
        try:
            if self.driver.find_element_by_css_selector(LoginPage.__username_icon).is_displayed():
                return True
        except NoSuchElementException:
            return False

    def password_label(self):
        return self.driver.find_element_by_xpath(LoginPage.__password_label).text

    def is_password_icon_visible(self):
        try:
            if self.driver.find_element_by_css_selector(LoginPage.__password_icon).is_displayed():
                return True
        except NoSuchElementException:
            return False

    def is_twitter_icon_visible(self):
        try:
            if self.driver.find_element_by_css_selector(LoginPage.__twitter_icon).is_displayed():
                return True
        except NoSuchElementException:
            return False

    def is_facebook_icon_visible(self):
        if self.driver.find_element_by_css_selector(LoginPage.__facebook_icon).is_displayed():
            return True
        else:
            return False

    def is_linkedin_icon_visible(self):
        try:
            if self.driver.find_element_by_css_selector(LoginPage.__facebook_icon).is_displayed():
                return True
        except NoSuchElementException:
            return False

    def is_remember_me_visible(self):
        try:
            if self.driver.find_element_by_css_selector(LoginPage.__remember_me).is_displayed():
                return True
        except NoSuchElementException:
            return False

    def login_user(self, username, password):
        username_field = self.driver.find_element_by_css_selector(LoginPage.__username)
        password_field = self.driver.find_element_by_css_selector(LoginPage.__password)
        username_field.clear()
        username_field.send_keys(username)
        password_field.clear()
        password_field.send_keys(password)
        self.driver.find_element_by_css_selector(LoginPage.__login_btn).click()

    def login_error_message(self):
        return self.driver.find_element_by_css_selector(LoginPage.__login_error).text
