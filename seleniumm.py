from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

driver1 = webdriver.Chrome()
driver2 = webdriver.Chrome()
driver3 = webdriver.Chrome()

driver1.get("https://www.youtube.com/")
driver2.get("https://digitalent.kominfo.go.id/")
driver3.get("https://www.cisco.com/")

username = browser.find_element_by_id("email")
password = browser.find_element_by_id("pass")
submit   = browser.find_element_by_id("loginbutton")
username.send_keys("you@email.com")
password.send_keys("yourpassword")

submit.click()
