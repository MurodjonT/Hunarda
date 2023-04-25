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

    """home page locators"""
    add_course_btn = (By.XPATH,
                      "//*[@class = \"v-btn v-theme--light bg-success v-btn-"
                      "-density-default v-btn--size-default v-btn--variant-flat\"]")
    input_name_field = (By.XPATH, "//*[text() = \"Name\"]/parent::div/div/div/div/div[3]/input")
    input_category_dropdwon = (By.XPATH, "//input[@type='search' and @placeholder = \"Categories\"]")
    in_input_category = (By.XPATH, "//li[contains(.,'IT')]")
    input_tag_dropdown = (By.XPATH, "//input[@type='search' and @placeholder = \"Tags\"]")
    in_tag = (By.XPATH, "//li[contains(.,'tag 12')]")
    upload_file = (By.XPATH, "//*[@type=\"file\"]")
    save_add_course = (By.XPATH, "//*[@class=\"v-btn v-btn--elevated v-theme--light bg-primary v-btn-"
                                 "-density-default v-btn--size-default v-btn--variant-elevated\"]")
    success_path = (By.XPATH, "//*[text()=\"Success\"]")

    input_search_course = (By.XPATH, "//*[@placeholder=\"Search\"]")

    edit_course_btn = (By.XPATH, "//*[text() = \"IT\"]/parent::tr/td[10]/div/button")
    x_icon_network = (By.XPATH, "/html/body/div[3]/div/div[2]/div/div[3]/form/div[2]/div[1]/div[1]/div/div[2]/button")

    in_edit_tag = (By.XPATH, "//li[contains(.,'tag')]")
    edit_category_dropdown = (By.XPATH, '/html/body/div[3]/div/div[2]/div/div[3]/form/div[2]/div[1]'
                                        '/div[1]/div/div[2]/button')
    x_icon_tag = (By.XPATH, "/html/body/div[3]/div/div[2]/div/div[3]/form/div[2]/div[2]/div[1]/div/div[1]/span/button")
    in_edit_category = (By.XPATH, "//li[contains(.,'Backend')]")
    delete_course_btn = (By.XPATH, "//*[text() = \"IT\"]/parent::tr/td[10]/button")
    confirm_delete = (By.XPATH, "//*[@class=\"swal2-confirm btn btn-success\"]")

    """Home page locators"""

    """ Staffs page Locators """
    Staff_btn = (By.XPATH, "//*[text() = \"Staffs\"]")
    add_staff_btn = (By.XPATH, "//*[@class=\"v-btn v-theme--light bg-success v-btn--density-default v-btn--size-default v-btn--variant-flat mt-7 float-right\"]")
    input_name_staff = (By.XPATH, "//*[@placeholder = \"Name\"]")
    input_password_staff = (By.XPATH, "//*[@type=\"password\"]")
    save_btn_staff = (By.XPATH, "//*[text() = \" Save \"]")

    """ Staffs page Locators End """

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

    def check_add_course(self, file, name):
        time.sleep(2)
        self.click(self.add_course_btn)
        time.sleep(2)
        self.click(self.input_category_dropdwon)
        time.sleep(2)
        self.click(self.in_input_category)
        time.sleep(1)
        self.click(self.input_tag_dropdown)
        time.sleep(1)
        self.click(self.in_tag)
        time.sleep(1)
        self.enter_data1(self.upload_file, file)
        self.enter_data1(self.input_name_field, name)
        time.sleep(1)
        self.click(self.save_add_course)
        try:
            if self.is_visible(self.success_path):
                return True
        except Exception:
            pass

    def check_edit_course(self, edit_name, edit_file):
        self.click(self.edit_course_btn)
        self.click(self.x_icon_network)
        self.click(self.input_category_dropdwon)
        time.sleep(1)
        self.click(self.in_input_category)
        time.sleep(1)
        self.click(self.x_icon_tag)
        self.click(self.input_tag_dropdown)
        time.sleep(1)
        self.click(self.in_edit_tag)
        time.sleep(1)
        self.enter_data(self.input_name_field, edit_name)
        self.enter_data1(self.upload_file, edit_file)
        self.click(self.save_add_course)
        try:
            if self.is_visible(self.success_path):
                return True
        except Exception:
            pass

    def check_delete_course(self):
        self.click(self.delete_course_btn)
        self.click(self.confirm_delete)
        try:
            if self.is_visible(self.success_path):
                return True
        except Exception:
            pass

    def check_search_course(self, search_name):
        self.enter_data(self.input_search_course, search_name)
        self.clear_field(self.input_search_course)
