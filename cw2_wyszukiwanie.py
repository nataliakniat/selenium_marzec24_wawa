import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# inicjalizacja przegladarki Chrome
driver = webdriver.Chrome()

url = "https://www.google.com"

# uruchomienie z konkretnym adresm
driver.get(url)

# maksymalizacja okna
driver.maximize_window()

# zaakceptuj zgody
accept = driver.find_element("id", "L2AGLb")
accept.click()

# wyszukiwarka
search = driver.find_element("name", "q")
search.send_keys("Pogoda")
search.send_keys(Keys.ENTER)
# search.submit()

time.sleep(600)

# zamknicie przegladarki
driver.quit()
