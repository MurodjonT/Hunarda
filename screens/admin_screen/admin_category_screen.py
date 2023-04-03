import time
from screens.screen import Screen
from selenium.webdriver.common.by import By


class CategoryPageScreen(Screen):

    def __init__(self, driver):
        super().__init__(driver)

    """ Add category locators"""
    directory_btn = (By.XPATH, "//span[text() = \"Directory\"]")
    add_category = (By.XPATH, "//*[@class=\"v-btn v-theme--light bg-success v-btn--density-default "
                              "v-btn--size-default v-btn--variant-flat\"]")
    input_name_category = (By.XPATH, "//*[@placeholder=\"Name\"]")
    upload_image = (By.XPATH, '//*[@type="file"]')
    save_btn_add_category = (By.XPATH, '//*[text() ="Save"]')
    """ Add category locators ends"""

    """ Edit category locators"""
    edit_btn_test_category = (By.XPATH, "//*[text() = \"test_category\"]/ancestor::tr/td[4]/div/div/button")
    delete_btn_category = (By.XPATH, "//*[text() = \"test_category_edit\"]/ancestor::tr/td[4]/div/button")
    confirm_delete = (By.XPATH, '//*[text() = "Yes, delete it!"]')
    """ Edit category locators Ends"""

    success_path = (By.XPATH, "//*[text()=\"Success\"]")

    def check_add_category(self, name_category, image_category):
        self.click(self.directory_btn)
        self.click(self.add_category)
        time.sleep(1)
        self.enter_data(self.input_name_category, name_category)
        self.enter_data1(self.upload_image, image_category)
        self.click(self.save_btn_add_category)
        try:
            if self.is_visible(self.success_path):
                return True
        except Exception:
            return False

    def check_edit_category(self, edit_name, edit_image):
        time.sleep(1)
        self.click(self.edit_btn_test_category)
        time.sleep(1)
        self.clear_field(self.input_name_category)
        time.sleep(1)
        self.enter_data(self.input_name_category, edit_name)
        self.enter_data1(self.upload_image, edit_image)
        self.click(self.save_btn_add_category)
        try:
            if self.is_visible(self.success_path):
                return True
        except Exception:
            return False

    def check_delete_category(self):
        time.sleep(1)
        self.click(self.delete_btn_category)
        self.click(self.confirm_delete)
        try:
            if self.is_visible(self.success_path):
                return True
        except Exception:
            return False
