from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

# implicitly wait - oczekiwanie na pojawienie się każdego elementu na stronie przez maksymalnie X sekund
driver.implicitly_wait(10)

driver.get("https://www.w3schools.com/")
driver.maximize_window()

# zaakceptuj ciasteczka
driver.find_element("id","accept-choices").click()

# wybranie menu "Tutorials"
menu = driver.find_element("id", "navbtn_tutorials")
# menu.click()

# klikanie za pomoca akcji
webdriver.ActionChains(driver).move_to_element(menu).click().perform()

# wybranie tutoriala 'learn HTML'
learnHTML = driver.find_element("xpath", "//a[@title='HTML Tutorial']")
learnHTML.click()

# wybranie menu 'Input types'
menuInput = driver.find_element("xpath", "//*[@id='leftmenuinnerinner']/a[43]")
menuInput.click()

time.sleep(600)
driver.quit()
