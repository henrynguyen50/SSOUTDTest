from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from dotenv import load_dotenv
import os

# Load login credentials from .env
load_dotenv()
USERNAME = os.getenv("UTDUSERNAME")
PASSWORD = os.getenv("UTDPASSWORD")

driver = webdriver.Chrome()

# Navigate to Galaxy page and click Orion
driver.get("https://www.utdallas.edu/galaxy/")
try:
    elem = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Orion"))
    )
finally:
    elem.click()

# Wait for and fill in login form
try:
    elem = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.NAME, "j_username"))
    )
finally:
    elem.send_keys(USERNAME)

try:
    elem = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.NAME, "j_password"))
    )
finally:
    elem.send_keys(PASSWORD)
    elem.send_keys(Keys.RETURN)

# Wait for "Yes, this is my device" button after DUO
try:
    element = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.ID, "trust-browser-button"))
    )
finally:
    element.click()

# Wait for Orion main page to fully load
try:
    element = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, "pt_pageinfo"))
    )
finally:
    pass

# Open eLearning in a new tab
driver.switch_to.new_window('tab')
driver.get("https://elearning.utdallas.edu/")

# Open VPN login page
driver.switch_to.new_window('tab')
driver.get("https://utdvpn.utdallas.edu/")

# Open Box login page and click continue
driver.switch_to.new_window('tab')
driver.get("https://utdallas.account.box.com/login")
try:
    elem = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div/div[1]/div/div[1]/form"))
    )
finally:
    elem.click()
    time.sleep(2)


# Open TouchNet payment portal
driver.switch_to.new_window('tab')
driver.get("https://idp.utdallas.edu/idp/profile/SAML2/Unsolicited/SSO?providerId=touchnet-prod-tbp")

time.sleep(10)
driver.quit()  # use quit to close all tabs/windows
