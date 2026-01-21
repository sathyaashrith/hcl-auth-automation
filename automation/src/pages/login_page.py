from selenium.webdriver.common.by import By
from automation.src.pages.base_page import BasePage

class LoginPage(BasePage):
    EMAIL = (By.ID, "email")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "loginBtn")
    MESSAGE_BOX = (By.ID, "messageBox")
    FORGOT_LINK = (By.ID, "forgotLink")

    def login(self, email, password):
        self.type_text(self.EMAIL, email)
        self.type_text(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)

    def get_message(self):
        return self.get_text(self.MESSAGE_BOX)

    def go_to_forgot_password(self):
        self.click(self.FORGOT_LINK)
