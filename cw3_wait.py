from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

# implicitly wait - oczekiwanie na pojawienie się każdego elementu na stronie przez maksymalnie X sekund
# driver.implicitly_wait(10)

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

# explicity wait - oczekiwanie na ten jeden konkretny element
wait = WebDriverWait(driver, 10, 0.5)
# warunek z dostępnej biblioteki
#wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='leftmenuinnerinner']/a[43]")))
# warunek własny
wait.until(lambda x: len(x.find_elements("xpath", "//*[@id='leftmenuinnerinner']/a[430]")))

# wybranie menu 'Input types'
menuInput = driver.find_element("xpath", "//*[@id='leftmenuinnerinner']/a[43]")
menuInput.click()

time.sleep(600)
driver.quit()
