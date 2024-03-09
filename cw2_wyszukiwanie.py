import time
from selenium import webdriver

# inicjalizacja przegladarki Chrome
driver = webdriver.Chrome()

url = "https://www.google.com"

# uruchomienie z konkretnym adresm
driver.get(url)

# maksymalizacja okna
driver.maximize_window()

time.sleep(60)

# zamknicie przegladarki
driver.quit()
