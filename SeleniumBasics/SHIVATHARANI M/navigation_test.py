"""
===========================================================
Hands-On 4 : WebDriver Navigation & Window Commands
Filename : navigation_test.py
===========================================================

Question 28
------------
1. Open Selenium Playground.
2. Click "Simple Form Demo".
3. Verify URL contains "simple-form-demo".
4. Navigate back.

Question 29
------------
1. Open Google in a new tab.
2. List all browser tabs.
3. Switch to Google tab.
4. Print Google title.

Question 30
------------
1. Switch back to Selenium Playground.
2. Take a screenshot.

Question 31
------------
1. Get browser window size.
2. Change window size.
3. Print updated size.

"""

import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# -------------------------------------------------------
# Launch Chrome
# -------------------------------------------------------

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

driver.maximize_window()

driver.get("https://www.lambdatest.com/selenium-playground/")

print("Current Page :", driver.title)

driver.implicitly_wait(10)

# -------------------------------------------------------
# Question 28
# Navigate to Simple Form Demo
# -------------------------------------------------------

print("\nNavigating to Simple Form Demo...")

simple_form = driver.find_element(
    By.LINK_TEXT,
    "Simple Form Demo"
)

simple_form.click()

print("Current URL :", driver.current_url)

assert "simple-form-demo" in driver.current_url

print("URL Verification Successful")

time.sleep(2)

driver.back()

print("Returned to Home Page")

# -------------------------------------------------------
# Question 29
# Open Google in New Tab
# -------------------------------------------------------

print("\nOpening Google in New Tab...")

driver.execute_script(
    'window.open("https://www.google.com");'
)

handles = driver.window_handles

print("\nWindow Handles")

for index, handle in enumerate(handles):
    print(f"Tab {index} : {handle}")

driver.switch_to.window(handles[1])

print("\nGoogle Page Title")

print(driver.title)

# -------------------------------------------------------
# Question 30
# Screenshot
# -------------------------------------------------------

driver.switch_to.window(handles[0])

print("\nBack to Selenium Playground")

# Create screenshots folder

os.makedirs("screenshots", exist_ok=True)

driver.save_screenshot(
    "screenshots/playground_screenshot.png"
)

print("Screenshot Saved")

# Verify

if os.path.exists("screenshots/playground_screenshot.png"):
    print("Screenshot Verified Successfully")
else:
    print("Screenshot Not Found")

# -------------------------------------------------------
# Question 31
# Window Size
# -------------------------------------------------------

print("\nCurrent Window Size")

size = driver.get_window_size()

print(size)

driver.set_window_size(1280, 800)

print("\nUpdated Window Size")

print(driver.get_window_size())

# Consistent browser window size is important because
# responsive web pages may display elements differently
# at different screen resolutions. Maintaining a fixed
# size ensures reliable Selenium automation.

time.sleep(2)

driver.quit()

print("\nBrowser Closed Successfully")