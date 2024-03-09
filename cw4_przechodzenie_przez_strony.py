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

# wybranie menu 'Tag list'
menuTag = driver.find_element("xpath", "//*[@id='leftmenuinnerinner']/a[67]")
menuTag.click()

# wybranie menu 'Input'
menuInput = driver.find_element("xpath", "//*[@id='leftmenuinnerinner']/div/a[59]")
menuInput.click()

# wybranie menu 'Disable'
menuDisable = driver.find_element("xpath", "//*[@id='main']/table[2]/tbody/tr[8]/td[1]/a")
menuDisable.click()

# klikniecie 'Try it yourself'
tryIt = driver.find_element("xpath", "//*[@id='main']/div[2]/a")
tryIt.click()

print("Aktualne okno: ", driver.title)

# obecna zakładka (okno)
currentWindow = driver.current_window_handle

# wszystkie zakładki (okna)
windowsNames = driver.window_handles

for window in windowsNames:
    if window != currentWindow:
        driver.switch_to.window(window)

print("Aktualne okno po przełączeniu: ", driver.title)

# przełączenie do ramki
driver.switch_to.frame(driver.find_element("id", "iframeResult"))

# wprowadzenie imienia
fname = driver.find_element("id", "fname")
fname.send_keys("Natalia")

lname = driver.find_element("id", "lname")
if lname.is_enabled():
    lname.send_keys("Burda")
else:
    print("Nie można wpisac nazwiska")

# zamkniecie zakładki
driver.close()

driver.switch_to.window(currentWindow)
print("Aktualne okno po powrocie: ", driver.title)

# cofniecie się
driver.back()

# wybranie menu 'Checkbox'
menuCheckbox = driver.find_element("xpath", "//*[@id='main']/table[2]/tbody/tr[6]/td[1]/a")
menuCheckbox.click()

# klikniecie 'Try it yourself'
tryIt = driver.find_element("xpath", "//*[@id='main']/div[2]/a")
tryIt.click()

print("Aktualne okno: ", driver.title)

# obecna zakładka (okno)
currentWindow = driver.current_window_handle

# wszystkie zakładki (okna)
windowsNames = driver.window_handles

for window in windowsNames:
    if window != currentWindow:
        driver.switch_to.window(window)

print("Aktualne okno po przełączeniu: ", driver.title)

# przełączenie do ramki
driver.switch_to.frame(driver.find_element("id", "iframeResult"))

# zaznaczanie checkboxa
bike = driver.find_element("name", "vehicle1")
bike.click()

if bike.is_selected():
    print("Poprawnie zaznaczono")

# wroc do poprzedniego okna TO DO

time.sleep(5)
driver.quit()
