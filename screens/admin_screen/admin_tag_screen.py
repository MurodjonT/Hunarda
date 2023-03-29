import time
from screens.screen import Screen
from selenium.webdriver.common.by import By


class TagPageScreen(Screen):

    def __init__(self, driver):
        super().__init__(driver)

    """Add tag locators"""
    directory_btn = (By.XPATH, "//span[text() = \"Directory\"]")
    tag_btn = (By.XPATH, '//span[text() = "Tags"]')
    add_tag_btn = (By.XPATH, '//span[text() = "Add"]')
    input_tag = (By.XPATH, '//*[@placeholder="Name"]')
    save_btn_tag = (By.XPATH, '//span[text() = "Save"]')

    edit_btn_name_tag = (By.XPATH, '//*[text() = "test_tag"]/ancestor::tr/td[3]/div/div/button')
    delete_btn_name_tag = (By.XPATH, '//*[text() = "test_tag_edit"]/ancestor::tr/td[3]/div/button[2]')
    confirm_delete = (By.XPATH, '//*[text() = "Yes, delete it!"]')
    """Add tag locators"""
    success_path = (By.XPATH, "//*[text()=\"Success\"]")

    def check_add_tag(self, name_tag):
        self.click(self.directory_btn)
        self.click(self.tag_btn)
        self.click(self.add_tag_btn)
        self.enter_data1(self.input_tag, name_tag)
        self.click(self.save_btn_tag)
        try:
            if self.is_visible(self.success_path):
                return True
        except Exception:
            return False

    def check_edit_tag(self, edit_name):
        self.click(self.edit_btn_name_tag)
        self.enter_data(self.input_tag, edit_name)
        self.click(self.save_btn_tag)

    def check_delete_tag(self):
        self.click(self.delete_btn_name_tag)
        self.click(self.confirm_delete)
        try:
            if self.is_visible(self.success_path):
                return True
        except Exception:
            return False