import time
from screens.screen import Screen
from selenium.webdriver.common.by import By


class DirectoryPageScreen(Screen):

    def __init__(self, driver):
        super().__init__(driver)

    directory_btn = (By.XPATH, "//span[text() = \"Directory\"]")
    news_btn = (By.XPATH, '//*[text() = "News"]/parent::button')
    add_news_btn = (By.XPATH, "//*[@class='v-btn v-btn--icon v-theme--light text-white v-btn--density-default v-btn--size-small v-btn--variant-text bg-success mt-2 rounded float-right']")
    input_name_news = (By.XPATH, "//*[@placeholder = \"Name\"]")
    input_description_news = (By.XPATH, "//*[@data-placeholder=\"Ma`lumot kiriting\"]")
    upload_img_news = (By.XPATH, "//*[@type=\"file\"]")
    save_btn_news = (By.XPATH, '//*[text() = "Save"]')


    def check_add_news(self, name_news, description, file):
        time.sleep(1)
        self.click(self.directory_btn)
        self.click(self.news_btn)
        self.click(self.add_news_btn)
        self.enter_data(self.input_name_news, name_news)
        self.enter_data(self.input_description_news, description)
        self.enter_data1(self.upload_img_news, file)
        self.click(self.save_btn_news)