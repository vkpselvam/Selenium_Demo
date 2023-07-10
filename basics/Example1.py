import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def test_open_chrome():
    s=Service(ChromeDriverManager().install())
    driver=webdriver.Chrome(service=s)
    driver.get("http://www.facebook.com")
    driver.maximize_window()
    time.sleep(5)
    assert driver.title=="Facebook – log in or sign up"
    driver.close()