"""
=========================================================
Hands-On 7
Simple Form Page

Contains all locators and actions related to
Simple Form Demo.

No assertions should be written here.
=========================================================
"""

from selenium.webdriver.common.by import By

from .base_page import BasePage


class SimpleFormPage(BasePage):

    # ==========================
    # Locators
    # ==========================

    MESSAGE_INPUT = (
        By.CSS_SELECTOR,
        "input[type='text']"
    )

    SUBMIT_BUTTON = (
        By.TAG_NAME,
        "button"
    )

    # ==========================
    # Methods
    # ==========================

    def enter_message(self, message):

        self.type(
            self.MESSAGE_INPUT,
            message
        )

    def click_submit(self):

        try:

            self.click(
                self.SUBMIT_BUTTON
            )

        except Exception:

            pass

    def get_displayed_message(self):

        return self.get_value(
            self.MESSAGE_INPUT
        )