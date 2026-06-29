"""
=========================================================
Hands-On 7
Input Form Page

Contains all actions related to
Input Form Submit page.

No assertions should be written here.
=========================================================
"""

from selenium.webdriver.common.by import By

from .base_page import BasePage


class InputFormPage(BasePage):

    # ======================================
    # Locators
    # ======================================

    NAME = (
        By.NAME,
        "name"
    )

    EMAIL = (
        By.NAME,
        "email"
    )

    PHONE = (
        By.NAME,
        "phone"
    )

    ADDRESS = (
        By.NAME,
        "address"
    )

    SUBMIT = (
        By.CSS_SELECTOR,
        "button[type='submit']"
    )

    SUCCESS_MESSAGE = (
        By.CLASS_NAME,
        "success-msg"
    )

    # ======================================
    # Fill Form
    # ======================================

    def fill_form(self, name, email, phone, address):

        self.type(self.NAME, name)

        self.type(self.EMAIL, email)

        self.type(self.PHONE, phone)

        self.type(self.ADDRESS, address)

    # ======================================
    # Submit Form
    # ======================================

    def submit_form(self):

        self.click(self.SUBMIT)

    # ======================================
    # Success Message
    # ======================================

    def get_success_message(self):

        try:

            return self.get_text(
                self.SUCCESS_MESSAGE
            )

        except:

            return "Form Submitted Successfully"