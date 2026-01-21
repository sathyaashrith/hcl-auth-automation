from selenium.webdriver.common.by import By
from automation.src.pages.base_page import BasePage

class ForgotPasswordPage(BasePage):
    EMAIL = (By.ID, "forgotEmail")
    RESET_BTN = (By.ID, "resetBtn")
    MESSAGE_BOX = (By.ID, "messageBox")
    SUCCESS_BOX = (By.ID, "successBox")

    def reset_password(self, email):
        self.type_text(self.EMAIL, email)
        self.click(self.RESET_BTN)

    def get_message(self):
        return self.get_text(self.MESSAGE_BOX)

    def get_success_message(self):
        return self.get_text(self.SUCCESS_BOX)
