from selenium import webdriver
from selenium.webdriver.common.by import By
import random


def test_create_account_pass():
    mail = str(random.randint(0, 10000)) + "student@merito.pl"

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("http://seleniumdemo.com/?page_id=7")

    driver.find_element("id", "reg_email").send_keys(mail)
    driver.find_element("id", "reg_password").send_keys("MojeNieFajneHaslo")

    driver.find_element("name", "register").click()

    assert driver.find_element(By.LINK_TEXT, "Logout").is_displayed()


def test_create_account_failed():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("http://seleniumdemo.com/?page_id=7")

    driver.find_element("id", "reg_email").send_keys("student@merito.pl")
    driver.find_element("id", "reg_password").send_keys("MojeNieFajneHaslo")

    driver.find_element("name", "register").click()

    msg = "Error: An account is already registered with your email address. Please log in."

    assert msg in driver.find_element("xpath", "//*[@id='page-7']/div/section/div/div/div[1]/ul/li").text


