"""
===========================================================
Hands-On 4 : Selenium WebDriver Setup
Filename : setup_test.py
===========================================================

Question 24

Selenium Components

1. WebDriver
---------------
WebDriver is the core component of Selenium.
It acts as a bridge between Python code and the browser.
Commands such as click(), send_keys(), and get() are sent
through WebDriver to the browser using the browser driver
(ChromeDriver).

2. Selenium Grid
----------------
Selenium Grid allows execution of automation tests on
multiple machines, browsers and operating systems
simultaneously. It is mainly used for parallel execution
and cross-browser testing.

3. Selenium IDE
---------------
Selenium IDE is a browser extension used for
record-and-playback automation. It is useful for beginners
to generate Selenium scripts without writing code manually.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# ---------------------------------------------------
# Question 25
# Launch Chrome using webdriver-manager
# ---------------------------------------------------

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

# Open Selenium Playground
driver.get("https://www.lambdatest.com/selenium-playground/")

print("Current URL:", driver.current_url)
print("Page Title:", driver.title)

# Print Page Title
print("Page Title : ", driver.title)

# ---------------------------------------------------
# Question 26
# Implicit Wait
# ---------------------------------------------------

# Implicit Wait applies to every element lookup.
# Although easy to use, it is generally considered
# a bad practice because it waits globally for all
# elements. Explicit Waits are preferred because
# they wait only for specific elements.

driver.implicitly_wait(10)

print("Implicit Wait Added Successfully")

driver.quit()

print("Browser Closed Successfully")

# ---------------------------------------------------
# Question 27
# Headless Mode
# ---------------------------------------------------

print("\nRunning Browser in Headless Mode...\n")

options = webdriver.ChromeOptions()

options.add_argument("--headless=new")

headless_driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

headless_driver.get(
    "https://www.lambdatest.com/selenium-playground/"
)

print("Headless Page Title : ", headless_driver.title)

headless_driver.quit()

print("Headless Browser Closed Successfully")