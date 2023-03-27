import time
from screens.screen import Screen
from selenium.webdriver.common.by import By


class NewsPageScreen(Screen):

    def __init__(self, driver):
        super().__init__(driver)

    """Add news locators"""
    directory_btn = (By.XPATH, "//span[text() = \"Directory\"]")
    news_btn = (By.XPATH, '//*[text() = "News"]/parent::button')
    add_news_btn = (By.XPATH, "//*[@class='v-btn v-btn--icon v-theme--light text-white v-btn--density-default "
                              "v-btn--size-small v-btn--variant-text bg-success mt-2 rounded float-right']")
    input_name_news = (By.XPATH, "//*[@placeholder = \"Name\"]")
    input_description_news = (By.XPATH, "//*[@data-placeholder=\"Ma`lumot kiriting\"]")
    upload_img_news = (By.XPATH, "//*[@type=\"file\"]")
    save_btn_news = (By.XPATH, '//*[text() = "Save"]')
    name_news_for_clear = (By.XPATH, '//*[@placeholder="Name"]/parent::div')
    """Add news locators END"""

    """edit news locators"""
    edit_drop_btn_news = (By.XPATH, "//*[text() = \"test_news\"]/parent::div/div[2]/button")
    edit_btn_test_news = (By.XPATH, "//*[@class=\"v-card-actions\"]/button[1]")

    """edit news locators END"""

    """Add news to course Locators"""
    test_news_btn = (By.XPATH, "//*[text() = 'test_news']")
    add_course_news_btn = (By.XPATH, "//*[text() = ' Add ']")
    course_dropdown = (By.XPATH, "//form/div/div/div/div/div[3]/div")
    in_course_dropdown = (By.XPATH, '//div[5]/div[2]/div')
    click_blank = (By.XPATH, '//*[@class="v-card-item"]')
    save_btn_course = (By.XPATH, '//*[@class="v-btn v-btn--elevated v-theme--light '
                                 'bg-primary v-btn--density-default v-btn--size-default v-btn--variant-elevated"]')
    delete_btn_test_news = (By.XPATH, "//*[@class=\"v-card-actions\"]/button[2]")
    confirm_delete = (By.XPATH, '//*[text() = "Yes, delete it!"]')
    """Add news to course Locators END"""

    success_path = (By.XPATH, "//*[text()=\"Success\"]")

    def check_add_news(self, name_news, description, file):
        time.sleep(1)
        self.click(self.directory_btn)
        self.click(self.news_btn)
        self.click(self.add_news_btn)
        self.enter_data(self.input_name_news, name_news)
        self.enter_data(self.input_description_news, description)
        self.enter_data1(self.upload_img_news, file)
        self.click(self.save_btn_news)

    def check_add_course_news(self):
        self.click(self.test_news_btn)
        self.click(self.add_course_news_btn)
        self.click(self.course_dropdown)
        self.click(self.in_course_dropdown)
        self.click(self.click_blank)
        self.click(self.save_btn_course)

    def check_edit_test_news(self, edit_name_news, edit_description, edit_file):
        self.click(self.edit_drop_btn_news)
        self.click(self.edit_btn_test_news)
        time.sleep(3)
        self.clear_field(self.input_name_news)
        time.sleep(1)
        self.enter_data(self.input_name_news, edit_name_news)
        time.sleep(1)
        self.clear_field(self.input_description_news)
        time.sleep(1)
        self.enter_data(self.input_description_news, edit_description)
        time.sleep(1)
        self.enter_data1(self.upload_img_news, edit_file)
        self.click(self.save_btn_news)

    def check_delete_test_news(self):
        self.click(self.edit_drop_btn_news)
        self.click(self.delete_btn_test_news)
        self.click(self.confirm_delete)
        try:
            if self.is_visible(self.success_path):
                return True
        except Exception:
            pass