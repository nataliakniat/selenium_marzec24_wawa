from selenium import webdriver
from selenium.webdriver.common.by import By


def test_login_pass():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("http://seleniumdemo.com/?page_id=7")

    driver.find_element("id", "username").send_keys("student@merito.pl")
    driver.find_element("id", "password").send_keys("MojeFajneHaslo")

    driver.find_element("name", "login").click()

    assert driver.find_element(By.LINK_TEXT, "Logout").is_displayed()


def test_login_failed():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("http://seleniumdemo.com/?page_id=7")

    driver.find_element("id", "username").send_keys("student@merito.pl")
    driver.find_element("id", "password").send_keys("MojeNieFajneHaslo")

    driver.find_element("name", "login").click()

    msg = "ERROR: Incorrect username or password"

    assert msg in driver.find_element("xpath", "//*[@id='page-7']/div/section/div/div/div[1]/ul/li").text


