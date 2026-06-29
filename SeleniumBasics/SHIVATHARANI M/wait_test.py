"""
===========================================================
Hands-On 5 : WebDriverWait & Expected Conditions
Filename : wait_test.py
===========================================================

Question 36
------------
Wait for Bootstrap Success Alert.

Question 37
------------
Compare time.sleep() vs Explicit Wait.

Question 38
------------
Use element_to_be_clickable().

Question 39
------------
Demonstrate Fluent Wait.
"""

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException
)

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

driver.maximize_window()
driver.implicitly_wait(5)

# =========================================================
# Question 36
# =========================================================

print("=" * 60)
print("QUESTION 36")
print("=" * 60)

driver.get(
    "https://www.testmuai.com/selenium-playground/bootstrap-alert-messages-demo/"
)

try:

    # Wait until Success button is clickable

    success_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//button[contains(.,'Success')]"
            )
        )
    )

    success_btn.click()

    print("Success Button Clicked")

    # Wait until alert is visible

    success_alert = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (
                By.CSS_SELECTOR,
                ".alert-success"
            )
        )
    )

    print("Alert Text :")
    print(success_alert.text)

    assert "success" in success_alert.text.lower()

    print("Alert Verification Successful")

except Exception as e:

    print("Bootstrap Alert page has changed.")
    print(e)

# =========================================================
# Question 37
# =========================================================

print("\n" + "=" * 60)
print("QUESTION 37")
print("=" * 60)

driver.refresh()

try:

    start = time.time()

    success_btn = driver.find_element(
        By.XPATH,
        "//button[contains(.,'Success')]"
    )

    success_btn.click()

    time.sleep(3)

    end = time.time()

    print(f"time.sleep() Execution : {end-start:.2f} seconds")

except:

    print("Sleep Example Skipped")

driver.refresh()

try:

    start = time.time()

    success_btn = WebDriverWait(driver,10).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//button[contains(.,'Success')]"
            )
        )
    )

    success_btn.click()

    WebDriverWait(driver,10).until(
        EC.visibility_of_element_located(
            (
                By.CSS_SELECTOR,
                ".alert-success"
            )
        )
    )

    end = time.time()

    print(f"Explicit Wait Execution : {end-start:.2f} seconds")

    print("""
Explicit Wait is preferred because:

• It waits only until the condition becomes true.
• It is faster on fast systems.
• It is more reliable on slow systems.
• Avoids unnecessary waiting.
""")

except:

    print("Explicit Wait Example Skipped")

# =========================================================
# Question 38
# =========================================================

print("\n" + "=" * 60)
print("QUESTION 38")
print("=" * 60)

try:

    clickable = WebDriverWait(driver,10).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//button[contains(.,'Success')]"
            )
        )
    )

    clickable.click()

    print("element_to_be_clickable() Demonstrated Successfully")

except:

    print("Clickable Element Example Skipped")

print("""

Difference

visibility_of_element_located()

✓ Element is visible.

element_to_be_clickable()

✓ Element is visible.
✓ Element is enabled.
✓ Element is not covered by another element.

""")

# =========================================================
# Question 39
# =========================================================

print("=" * 60)
print("QUESTION 39")
print("=" * 60)

driver.get(
    "https://www.testmuai.com/selenium-playground/table-sort-search-demo/"
)

try:

    wait = WebDriverWait(
        driver,
        timeout=10,
        poll_frequency=0.5,
        ignored_exceptions=[NoSuchElementException]
    )

    row = wait.until(
        EC.visibility_of_element_located(
            (
                By.TAG_NAME,
                "table"
            )
        )
    )

    print("Fluent Wait Successful")
    print("Table Loaded Successfully")

except TimeoutException:

    print("Fluent Wait Timed Out")

driver.quit()

print("\nBrowser Closed Successfully")