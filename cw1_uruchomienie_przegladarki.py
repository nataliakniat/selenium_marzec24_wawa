import time
from selenium import webdriver

# inicjalizacja przegladarki Chrome
driver = webdriver.Chrome()

# uruchomienie z konkretnym adresm
driver.get("https://www.google.com")

time.sleep(60)

# zamknicie przegladarki
driver.quit()
