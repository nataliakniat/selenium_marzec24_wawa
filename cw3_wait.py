from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://www.w3schools.com/")
driver.maximize_window()

# zaakceptuj ciasteczka
driver.find_element("id","accept-choices").click()

# wybranie menu "Tutorials"
menu = driver.find_element("id", "navbtn_tutorials")
menu.click()

time.sleep(600)
driver.quit()
