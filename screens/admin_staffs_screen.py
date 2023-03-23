import time

from screens.screen import Screen
from selenium.webdriver.common.by import By


class StaffPageScreen(Screen):

    def __init__(self, driver):
        super().__init__(driver)

    """ Staffs page Locators """
    Staff_btn = (By.XPATH, "//*[text() = \"Staffs\"]")
    add_staff_btn = (By.XPATH, "//*[@class='v-btn v-theme--light bg-success v-btn--density-default v-btn--size-default v-btn--variant-flat mt-7 float-right']")
    input_name_staff = (By.XPATH, "//*[@placeholder = \"Name\"]")
    input_password_staff = (By.XPATH, "//*[@type=\"password\"]")
    save_btn_staff = (By.XPATH, "//*[text() = \" Save \"]")

    edit_btn_staff = (By.XPATH, "//*[text() = \"Mirtesha\"]/parent::div/parent::td/parent::tr/td[4]/div/a")
    input_first_name = (By.XPATH, "//*[@placeholder=\"First Name\"]")
    input_surname_name = (By.XPATH, "[placeholder=\"Surname\"]")
    input_email = (By.XPATH, "//*[@placeholder=\"E-mail\"]")
    input_number = (By.XPATH, "//*[@placeholder=\"Phone number\"]")
    role_dropdown = (By.XPATH, "//div[3]/div/div/div/div/div[3]/div")
    in_role = (By.XPATH, "//body/div[3]/div/div/div/div/div[2]/div")

    """ Staffs page Locators End """
    success_path = (By.XPATH, "//*[text()=\"Success\"]")
    def check_add_staff(self, name, password):
        time.sleep(2)
        self.click(self.Staff_btn)
        self.click(self.add_staff_btn)
        self.enter_data(self.input_name_staff, name)
        self.enter_data(self.input_password_staff, password)
        self.click(self.save_btn_staff)
        try:
            if self.is_visible(self.success_path):
                return True
        except Exception:
            pass

    def check_edit_staff(self, first_name, surname, email, number):
        self.click(self.edit_btn_staff)
        self.enter_data1(self.input_first_name, first_name)
        self.enter_data1(self.input_email, surname)
        self.enter_data1(self.input_email, email)
        self.enter_data1(self.input_number, number)
        self.click(self.role_dropdown)
        self.click(self.in_role)
