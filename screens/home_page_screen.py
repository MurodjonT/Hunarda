import time

from screens.screen import Screen
from selenium.webdriver.common.by import By


class HomePageScreen(Screen):

    def __init__(self, driver):
        super().__init__(driver)

    """login_page locator"""
    login_field = (
        By.XPATH, "/html/body/div[1]/div/div/div/div/div/div/div[3]/div[4]/form/div/div[1]/div/div/div/div[3]/input")
    password_field = (By.XPATH, "//*[@type=\"password\"]")
    login_btn = (By.XPATH, '//*[@class="v-btn__content"]')
    success_login = (By.XPATH, "//*[text()=\"Login success\"]")
    """login_page locator END"""

    """Staffs page locators"""
    add_course_btn = (By.XPATH,
                      "//*[@class = \"v-btn v-theme--light bg-success v-btn--density-default v-btn--size-default v-btn--variant-flat\"]")
    input_name_field = (By.XPATH, "//*[text() = \" Name \"]/parent::div/div/div/div/div[3]/input")
    input_category_dropdwon = (
        By.XPATH, "/html/body/div[3]/div/div[2]/div/div[3]/form/div[2]/div[1]/div/div/div/div[3]/div")
    in_input_category = (By.XPATH, "//div[2]/div/div/div[2]/div[2]/div")
    input_tag_dropdown = (By.XPATH, "//*[text() = \" Tag \"]/parent::div/div/div/div/div[3]/div/input")
    in_tag = (By.XPATH, "//*[contains(.,'tags')]")
    """Staffs page locators"""

    def check_open_home_page(self, login, password):
        time.sleep(2)
        self.enter_data1(self.login_field, login)
        self.enter_data1(self.password_field, password)
        self.click(self.login_btn)
        try:
            if self.is_visible(self.success_login):
                return True
        except Exception:
            pass

    def check_add_course(self):
        time.sleep(2)
        self.click(self.add_course_btn)
        time.sleep(2)
        self.click(self.input_category_dropdwon)
        time.sleep(2)
        self.click(self.in_input_category)
