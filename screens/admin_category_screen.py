import time
from screens.screen import Screen
from selenium.webdriver.common.by import By


class CategoryPageScreen(Screen):

    def __init__(self, driver):
        super().__init__(driver)
