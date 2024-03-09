from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://www.w3schools.com/")
driver.maximize_window()

# zaakceptuj ciasteczka
driver.find_element("id","accept-choices").click()

# wybranie menu "Tutorials"
menu = driver.find_element("id", "navbtn_tutorials")
# menu.click()

# klikanie za pomoca akcji
# webdriver.ActionChains(driver).move_to_element(menu).perform()
webdriver.ActionChains(driver).move_to_element(menu).click().perform()

# wybranie tutoriala 'learn HTML'
# po xpath skopiowanym z narzedzi developerskich
#learnHTML = driver.find_element("xpath", "//*[@id='tutorials_html_css_links_list']/div[1]/a[1]")
# po xpath pisanym 'z palca'
learnHTML = driver.find_element("xpath", "//a[@title='HTML Tutorial']")
learnHTML.click()

time.sleep(600)
driver.quit()
