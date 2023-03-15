import pytest
from selenium.webdriver.chrome.service import Service as serv
from selenium import webdriver
import time


@pytest.fixture(params=['chrome'], scope='class')
def init_driver(request):
    global web_driver
    s = serv("C:\\Program Files\\Drivers\\chromedriver_win32\\chromedriver.exe")
    web_driver = webdriver.Chrome(service=s)
    web_driver.maximize_window()
    web_driver.get("http://192.168.31.103:5173/")
    web_driver.implicitly_wait(10)
    request.cls.driver = web_driver
    yield
    time.sleep(5)
    web_driver.close()

