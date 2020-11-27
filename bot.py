from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

# Navigate to url
driver.get("https://docs.google.com/forms/u/3/")

# Store 'google search' button web element
make_form_button = driver.find_element_by_id(":1g")

# Perform click-and-hold action on the element
webdriver.ActionChains(driver).click_and_hold(make_form_button).perform()

time.sleep(5)