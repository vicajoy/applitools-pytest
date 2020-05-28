from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class LoginPage:

    __page_title = (By.CLASS_NAME, "auth-header")
    __username_icon = (By.CLASS_NAME, "os-icon-user-male-circle")
    __password_icon = (By.CLASS_NAME, "os-icon-fingerprint")
    __twitter_icon = (By.CSS_SELECTOR, "img[src='img/social-icons/twitter.png']")
    __facebook_icon = (By.CSS_SELECTOR, "img[src='img/social-icons/facebook.png']")
    __linkedin_icon = (By.CSS_SELECTOR, "img[src='img/social-icons/linkedin.png']")
    __remember_me = (By.CLASS_NAME, "form-check-label")
    __username_label = (By.XPATH, "//input[@id='username']/../label")
    __password_label = (By.XPATH, "//input[@id='password']/../label")
    __login_btn = (By.ID, "log-in")
    __login_error = (By.CLASS_NAME, "alert-warning")
    __username = (By.ID, "username")
    __password = (By.ID, "password")

    def __init__(self, driver):
        self.driver = driver

    def page_title(self):
        return self.driver.find_element(*self.__page_title).text

    def username_label(self):
        return self.driver.find_element(*self.__username_label).text

    def is_username_icon_visible(self):
        try:
            if self.driver.find_element(*self.__username_icon).is_displayed():
                return True
        except NoSuchElementException:
            return False

    def password_label(self):
        return self.driver.find_element(*self.__password_label).text

    def is_password_icon_visible(self):
        try:
            if self.driver.find_element(*self.__password_icon).is_displayed():
                return True
        except NoSuchElementException:
            return False

    def is_twitter_icon_visible(self):
        try:
            if self.driver.find_element(*self.__twitter_icon).is_displayed():
                return True
        except NoSuchElementException:
            return False

    def is_facebook_icon_visible(self):
        if self.driver.find_element(*self.__facebook_icon).is_displayed():
            return True
        else:
            return False

    def is_linkedin_icon_visible(self):
        try:
            if self.driver.find_element(*self.__facebook_icon).is_displayed():
                return True
        except NoSuchElementException:
            return False

    def is_remember_me_visible(self):
        try:
            if self.driver.find_element(*self.__remember_me).is_displayed():
                return True
        except NoSuchElementException:
            return False

    def login_user(self, username, password):
        username_field = self.driver.find_element(*self.__username)
        password_field = self.driver.find_element(*self.__password)
        username_field.clear()
        username_field.send_keys(username)
        password_field.clear()
        password_field.send_keys(password)
        self.driver.find_element(*self.__login_btn).click()

    def login_error_message(self):
        return self.driver.find_element(*self.__login_error).text
