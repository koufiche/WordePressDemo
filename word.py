import driver as driver
from selenium import webdriver
from selenium.webdriver import ActionChains
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://wordpress.com/me")
driver.find_element_by_css_selector("button[class='button gdpr-banner__acknowledge-button']").click()
driver.find_element_by_id("usernameOrEmail").click()
driver.find_element_by_name("usernameOrEmail").send_keys("smonaji01@gmail.com")
driver.find_element_by_css_selector("button[type='submit']").click()
driver.find_element_by_id("password").click()
driver.find_element_by_css_selector("input[type='password']").send_keys("Sm@Said")
driver.find_element_by_css_selector("button[class='button form-button is-primary'").click()
driver.find_element_by_id("first_name").click()
driver.find_element_by_name("first_name").send_keys("sm")
driver.find_element_by_id("last_name").click()
driver.find_element_by_css_selector("input[id='last_name']").click()
driver.find_element_by_class_name("description").click()
driver.find_element_by_id("description").send_keys("I am an IT professional looking for new opportunity")
driver.find_element_by_css_selector("button[type='submit'").click()

