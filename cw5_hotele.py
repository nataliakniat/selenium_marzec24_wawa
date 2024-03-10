from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("http://www.kurs-selenium.pl/")

# wprowadzenie nazwy miasta
driver.find_element("xpath", "//span[text()='Search by Hotel or City Name']").click()
driver.find_element("xpath", "//*[@id='select2-drop']/div/input").send_keys("Dubai")
driver.find_element("xpath", "//span[text()='Dubai']").click()

# wybranie daty
driver.find_element("name", "checkin").send_keys("10/03/2024")
driver.find_element("name", "checkout").send_keys("12/03/2024")

# wybranie liczby turystów
driver.find_element("id", "travellersInput").click()
driver.find_element("id", "adultInput").clear()
driver.find_element("id", "adultInput").send_keys("1")
driver.find_element("id", "childInput").clear()
driver.find_element("id", "childInput").send_keys("2")

# wyszukaj
driver.find_element("xpath", "//*[@id='hotels']/form/div[5]/button").click()

# wynik wyszukiwania
# hotels = driver.find_elements("xpath", "//h4[contains(@class, 'list_title')]")
# hotels_name = [hotel.get_attribute() for hotel in hotels]

time.sleep(500)
driver.quit()
