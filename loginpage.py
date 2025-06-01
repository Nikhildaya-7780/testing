from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    # Define the locators for login form
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-btn")

    def enter_username(self, username):
        self.type(*self.USERNAME_INPUT, username)

    def enter_password(self, password):
        self.type(*self.PASSWORD_INPUT, password)

    def click_login(self):
        self.click(*self.LOGIN_BUTTON)
