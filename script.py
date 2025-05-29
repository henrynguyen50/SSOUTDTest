from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
#getting login credentials
from dotenv import load_dotenv
import os
load_dotenv()
USERNAME = os.getenv("UTDUSERNAME")
PASSWORD = os.getenv("UTDPASSWORD")


driver = webdriver.Chrome()

#getting to orion then the login page
driver.get("https://www.utdallas.edu/galaxy/")
elem = driver.find_element(By.LINK_TEXT, "Orion")
elem.click()


#entering login credentials 
elem = driver.find_element(By.NAME, "j_username") 
elem.send_keys(USERNAME) #send username

elem = driver.find_element(By.NAME, "j_password") 
elem.send_keys(PASSWORD) #send pw
elem.send_keys(Keys.RETURN)

time.sleep(20)
driver.switch_to.new_window('tab')
driver.get("https://elearning.utdallas.edu/")

driver.switch_to.new_window('tab')
driver.get("https://utdvpn.utdallas.edu/")

driver.switch_to.new_window('tab')
driver.get("https://utdallas.account.box.com/login")
elem = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[1]/div/div[1]/form")
elem.click()


driver.switch_to.new_window('tab')
driver.get("https://idp.utdallas.edu/idp/profile/SAML2/Unsolicited/SSO?providerId=touchnet-prod-tbp")
