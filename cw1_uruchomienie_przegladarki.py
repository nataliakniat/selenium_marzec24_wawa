import time
from selenium import webdriver

# inicjalizacja przegladarki Chrome
driver = webdriver.Chrome()

url = "https://www.google.com"
new_url = "https://www.wp.pl"

# uruchomienie z konkretnym adresm
driver.get(url)

# maksymalizacja okna
driver.maximize_window()

# rozmiar okna na stałe
# driver.set_window_size(800, 400)

# otwarcie nowego okna
driver.execute_script("window.open('');")

# przełączenie sie do nowego okna
driver.switch_to.window(driver.window_handles[1])

# wpisanie nowgo adresu
driver.get(new_url)

# zamkniecie zakładki
driver.close()

time.sleep(60)

# zamknicie przegladarki
driver.quit()
